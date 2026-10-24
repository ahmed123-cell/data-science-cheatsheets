"""Integration Tests for Automated DVC Pipeline Execution."""

import json
from pathlib import Path
import joblib
import pandas as pd
from src.prepare import main as run_prepare
from src.train_mlflow import main as run_train
from src.evaluate import main as run_evaluate


def test_full_pipeline_execution(tmp_path: Path, monkeypatch):
    """Executes prepare -> train -> evaluate end-to-end and validates artifacts."""
    # Run prepare stage
    run_prepare()
    assert Path("data/processed/train.parquet").exists()
    assert Path("data/processed/val.parquet").exists()

    # Run train stage
    run_train()
    assert Path("models/pipeline.joblib").exists()

    # Run evaluate stage
    run_evaluate()
    metrics_file = Path("metrics.json")
    assert metrics_file.exists()

    with open(metrics_file, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    assert "val_mae" in metrics
    assert "val_rmse" in metrics
    assert "val_r2" in metrics
    assert metrics["val_mae"] > 0.0
    assert metrics["val_r2"] > 0.0

    # Test that model artifact can be loaded and predict
    model = joblib.load("models/pipeline.joblib")
    sample_df = pd.DataFrame([{
        "PULocationID": 43,
        "DOLocationID": 142,
        "trip_distance": 3.5,
        "passenger_count": 1,
        "hour_of_day": 14,
        "day_of_week": 2,
    }])
    pred = model.predict(sample_df)
    assert len(pred) == 1
    assert pred[0] > 0.0
