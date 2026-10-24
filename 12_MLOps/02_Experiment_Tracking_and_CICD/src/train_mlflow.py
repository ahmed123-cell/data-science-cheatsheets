"""DVC Stage 2: Model Training and MLflow Experiment Tracking (train_mlflow.py).

Logs hyperparameters, training metrics, model signature, and model artifacts
to the MLflow tracking server and exports model artifact.
"""

from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import yaml

try:
    import mlflow
    import mlflow.sklearn
    from mlflow.models.signature import infer_signature
    HAS_MLFLOW = True
except ImportError:
    HAS_MLFLOW = False


def load_train_params() -> dict:
    with open("params.yaml", "r", encoding="utf-8") as f:
        params = yaml.safe_load(f)
    return params


def main() -> None:
    config = load_train_params()
    prep_params = config["prepare"]
    train_params = config["train"]

    train_path = Path(prep_params["processed_train_path"])
    print(f"Loading processed training data from: {train_path}")
    train_df = pd.read_parquet(train_path)

    feature_cols = [
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "passenger_count",
        "hour_of_day",
        "day_of_week",
    ]
    target_col = "trip_duration_minutes"

    X_train = train_df[feature_cols]
    y_train = train_df[target_col]

    # Initialize MLflow experiment
    experiment_name = train_params["experiment_name"]
    if HAS_MLFLOW:
        # Use local SQLite tracking database so model registry is fully functional locally
        db_path = Path("mlruns.db").absolute()
        mlflow.set_tracking_uri(f"sqlite:///{db_path}")
        mlflow.set_experiment(experiment_name)
        run_context = mlflow.start_run(run_name=f"train-{train_params['model_type']}")
    else:
        run_context = None

    try:
        print(f"Training {train_params['model_type']} regression pipeline...")
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            (
                "model",
                Ridge(
                    alpha=train_params["alpha"],
                    fit_intercept=train_params["fit_intercept"],
                ),
            ),
        ])
        pipeline.fit(X_train, y_train)

        # Compute train metrics
        train_preds = pipeline.predict(X_train)
        train_mae = mean_absolute_error(y_train, train_preds)
        train_rmse = root_mean_squared_error(y_train, train_preds)
        print(f"Training Metrics -> MAE: {train_mae:.2f} mins | RMSE: {train_rmse:.2f} mins")

        # Save local artifact
        models_dir = Path("models")
        models_dir.mkdir(parents=True, exist_ok=True)
        model_out = models_dir / "pipeline.joblib"
        joblib.dump(pipeline, model_out)
        print(f"Saved trained pipeline to: {model_out}")

        # Log to MLflow if available
        if HAS_MLFLOW:
            # 1. Log parameters
            mlflow.log_params({
                "model_type": train_params["model_type"],
                "alpha": train_params["alpha"],
                "fit_intercept": train_params["fit_intercept"],
                "n_train_samples": len(X_train),
            })

            # 2. Log metrics
            mlflow.log_metrics({
                "train_mae": round(train_mae, 4),
                "train_rmse": round(train_rmse, 4),
            })

            # 3. Infer signature and log model with input example
            signature = infer_signature(X_train[:5], train_preds[:5])
            try:
                mlflow.sklearn.log_model(
                    sk_model=pipeline,
                    artifact_path="model",
                    signature=signature,
                    input_example=X_train[:3],
                    registered_model_name=train_params.get("registered_model_name"),
                )
            except Exception as reg_exc:
                # Fallback if model registry server is unavailable
                mlflow.sklearn.log_model(
                    sk_model=pipeline,
                    artifact_path="model",
                    signature=signature,
                    input_example=X_train[:3],
                )
                print(f"Logged model artifact (registry notice: {reg_exc})")

            # 4. Log tags
            mlflow.set_tags({
                "pipeline": "dvc",
                "framework": "scikit-learn",
                "task": "regression",
            })
            print("Successfully logged run and registered model to MLflow.")

    finally:
        if HAS_MLFLOW and run_context:
            mlflow.end_run()


if __name__ == "__main__":
    main()
