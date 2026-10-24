"""DVC Stage 1: Data Ingestion and Validation (prepare.py).

Cleanses raw data, filters invalid records, and splits into train and validation sets.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import yaml


def load_params() -> dict:
    with open("params.yaml", "r", encoding="utf-8") as f:
        params = yaml.safe_load(f)
    return params["prepare"]


def generate_raw_dataset_if_missing(file_path: Path, n_records: int = 10000) -> None:
    """Generates synthetic raw CSV if none exists."""
    if file_path.exists():
        return
    print(f"Raw data file {file_path} not found. Generating initial raw dataset...")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    np.random.seed(42)

    pu = np.random.randint(1, 265, size=n_records)
    do = np.random.randint(1, 265, size=n_records)
    distance = np.random.exponential(scale=3.5, size=n_records) + 0.1
    passengers = np.random.choice([1, 2, 3, 4], p=[0.75, 0.15, 0.07, 0.03], size=n_records)
    hour = np.random.randint(0, 24, size=n_records)
    dow = np.random.randint(0, 7, size=n_records)

    # Duration target in minutes
    duration = 4.5 + (distance * 2.7) + (hour * 0.12) + np.random.normal(0, 2.0, size=n_records)
    duration = np.clip(duration, 1.0, 180.0)

    df = pd.DataFrame({
        "PULocationID": pu,
        "DOLocationID": do,
        "trip_distance": np.round(distance, 2),
        "passenger_count": passengers,
        "hour_of_day": hour,
        "day_of_week": dow,
        "trip_duration_minutes": np.round(duration, 2),
    })
    df.to_csv(file_path, index=False)
    print(f"Created synthetic raw CSV at: {file_path}")


def main() -> None:
    params = load_params()
    raw_path = Path(params["raw_data_path"])
    generate_raw_dataset_if_missing(raw_path)

    print(f"Loading raw data from: {raw_path}")
    df = pd.read_csv(raw_path)
    initial_len = len(df)

    # 1. Validation & Cleansing
    min_dist = params["min_trip_distance"]
    max_dist = params["max_trip_distance"]
    df = df[(df["trip_distance"] >= min_dist) & (df["trip_distance"] <= max_dist)]
    df = df[(df["PULocationID"] >= 1) & (df["PULocationID"] <= 265)]
    df = df[(df["DOLocationID"] >= 1) & (df["DOLocationID"] <= 265)]
    df = df.dropna()

    print(f"Cleaned dataset: {len(df)} rows retained from {initial_len} initial records.")

    # 2. Train / Validation Split
    val_ratio = params["val_ratio"]
    seed = params["random_seed"]
    shuffled_idx = np.random.RandomState(seed=seed).permutation(len(df))
    split_point = int(len(df) * (1 - val_ratio))

    train_df = df.iloc[shuffled_idx[:split_point]]
    val_df = df.iloc[shuffled_idx[split_point:]]

    # 3. Export to efficient Parquet format
    train_path = Path(params["processed_train_path"])
    val_path = Path(params["processed_val_path"])
    train_path.parent.mkdir(parents=True, exist_ok=True)

    train_df.to_parquet(train_path, index=False)
    val_df.to_parquet(val_path, index=False)

    print(f"Saved train set ({len(train_df)} rows) to: {train_path}")
    print(f"Saved validation set ({len(val_df)} rows) to: {val_path}")


if __name__ == "__main__":
    main()
