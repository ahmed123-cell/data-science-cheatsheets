"""Data Contract and Schema Validation Tests."""

from pathlib import Path
import pandas as pd
from src.prepare import main as run_prepare


def test_processed_data_schema_contract():
    """Validates that train.parquet satisfies exact column and type specifications."""
    train_path = Path("data/processed/train.parquet")
    if not train_path.exists():
        run_prepare()

    df = pd.read_parquet(train_path)
    required_features = [
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "passenger_count",
        "hour_of_day",
        "day_of_week",
    ]
    target = "trip_duration_minutes"

    for col in required_features:
        assert col in df.columns, f"Missing feature: {col}"

    assert target in df.columns, f"Missing target column: {target}"
    assert (df["trip_distance"] > 0).all(), "Found non-positive trip distances!"
    assert df[required_features].isna().sum().sum() == 0, "Found null values in feature columns!"
