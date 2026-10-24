"""Inference Pattern 2: High-Throughput Batch Scoring Pipeline (batch_score.py).

Scores millions of records offline on a schedule (daily/weekly/monthly).
Reads Parquet from data lake, loads model once, vectors predictions, and outputs scored Parquet.
"""

from datetime import datetime, timezone
from pathlib import Path
import uuid
import numpy as np
import pandas as pd


def generate_batch_input_if_missing(file_path: Path, n_records: int = 50000) -> None:
    """Creates a sample batch file if not present."""
    if file_path.exists():
        return
    print(f"Generating synthetic batch input ({n_records} rows) at: {file_path}")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    np.random.seed(101)

    df = pd.DataFrame({
        "ride_id": [f"ride_{i:06d}" for i in range(n_records)],
        "PULocationID": np.random.randint(1, 265, size=n_records),
        "DOLocationID": np.random.randint(1, 265, size=n_records),
        "trip_distance": np.round(np.random.exponential(3.5, size=n_records) + 0.1, 2),
        "passenger_count": np.random.choice([1, 2, 3, 4], size=n_records),
        "hour_of_day": np.random.randint(0, 24, size=n_records),
        "day_of_week": np.random.randint(0, 7, size=n_records),
    })
    df.to_parquet(file_path, index=False)


def run_batch_scoring(
    input_parquet: Path,
    output_parquet: Path,
    model_version: str = "v1.0.0-production",
) -> None:
    """Executes high-throughput batch scoring."""
    start_time = datetime.now(timezone.utc)
    print(f"Starting batch scoring run at {start_time.isoformat()}...")
    print(f"Reading input dataset: {input_parquet}")

    df = pd.read_parquet(input_parquet)
    print(f"Loaded {len(df):,} records for batch scoring.")

    # Feature matrix extraction
    feature_cols = [
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "passenger_count",
        "hour_of_day",
        "day_of_week",
    ]
    X = df[feature_cols].to_numpy(dtype=np.float32)

    # High-speed vectorized scoring:
    # duration = 5.0 + (distance * 2.5) + (hour * 0.15)
    preds = 5.0 + (X[:, 2] * 2.5) + (X[:, 4] * 0.15)
    preds = np.round(np.clip(preds, 2.0, 180.0), 2)

    # Attach scoring audit metadata
    batch_run_id = str(uuid.uuid4())
    df["predicted_duration_minutes"] = preds
    df["model_version"] = model_version
    df["scoring_timestamp"] = datetime.now(timezone.utc).isoformat()
    df["batch_run_id"] = batch_run_id

    # Write output to scored data lake partitioned by date
    output_parquet.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_parquet, index=False)

    duration_sec = (datetime.now(timezone.utc) - start_time).total_seconds()
    throughput = len(df) / max(0.001, duration_sec)

    print("=" * 55)
    print("BATCH SCORING COMPLETED")
    print(f"  Records Processed:   {len(df):,}")
    print(f"  Execution Time:      {duration_sec:.2f} seconds")
    print(f"  Throughput:          {throughput:,.0f} records/second")
    print(f"  Batch Run ID:        {batch_run_id}")
    print(f"  Output Parquet:      {output_parquet}")
    print("=" * 55)


if __name__ == "__main__":
    raw_batch = Path("data/batch_input/rides_to_score.parquet")
    scored_batch = Path("data/batch_output/rides_scored.parquet")
    generate_batch_input_if_missing(raw_batch, n_records=50000)
    run_batch_scoring(raw_batch, scored_batch)
