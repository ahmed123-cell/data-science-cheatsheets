"""DVC Stage 3: Model Evaluation and Promotion Gate (evaluate.py).

Evaluates the trained pipeline on the holdout validation set, generates metrics.json,
and tests against production acceptance criteria.
"""

import json
from pathlib import Path
import joblib
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    root_mean_squared_error,
)
import yaml


def load_config() -> dict:
    with open("params.yaml", "r", encoding="utf-8") as f:
        params = yaml.safe_load(f)
    return params


def main() -> None:
    config = load_config()
    prep_params = config["prepare"]
    eval_params = config["evaluate"]

    val_path = Path(prep_params["processed_val_path"])
    model_path = Path("models/pipeline.joblib")

    print(f"Loading validation set from: {val_path}")
    val_df = pd.read_parquet(val_path)

    feature_cols = [
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "passenger_count",
        "hour_of_day",
        "day_of_week",
    ]
    target_col = "trip_duration_minutes"

    X_val = val_df[feature_cols]
    y_val = val_df[target_col]

    print(f"Loading trained pipeline from: {model_path}")
    pipeline = joblib.load(model_path)

    # Generate predictions
    preds = pipeline.predict(X_val)

    # Compute regression metrics
    val_mae = mean_absolute_error(y_val, preds)
    val_rmse = root_mean_squared_error(y_val, preds)
    val_r2 = r2_score(y_val, preds)

    metrics_payload = {
        "val_mae": round(float(val_mae), 4),
        "val_rmse": round(float(val_rmse), 4),
        "val_r2": round(float(val_r2), 4),
        "n_validation_samples": int(len(val_df)),
    }

    print("=" * 45)
    print("VALIDATION METRICS SUMMARY")
    print(f"  MAE:  {val_mae:.4f} mins")
    print(f"  RMSE: {val_rmse:.4f} mins")
    print(f"  R^2:  {val_r2:.4f}")
    print("=" * 45)

    # Write metrics.json for DVC and CI/CD consumption
    out_metrics_path = Path(eval_params["metrics_output_path"])
    with open(out_metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_payload, f, indent=2)
    print(f"Wrote metrics report to: {out_metrics_path}")

    # Production Promotion Gate
    threshold_mae = eval_params["target_max_mae"]
    if val_mae <= threshold_mae:
        print(f"PASS: Validation MAE ({val_mae:.2f}) meets acceptance threshold ({threshold_mae:.2f}).")
        print("Model is eligible for promotion to Staging / Production.")
    else:
        print(f"FAIL: Validation MAE ({val_mae:.2f}) exceeds threshold ({threshold_mae:.2f}).")
        raise ValueError("Model failed quality gate. Deployment aborted.")


if __name__ == "__main__":
    main()
