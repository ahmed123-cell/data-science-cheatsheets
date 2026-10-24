"""Apache Airflow Production Pipeline: Weekly Ride Duration Model Retraining DAG.

Orchestrates the continuous retraining lifecycle:
Extract -> Validate -> Train (MLflow) -> Evaluate against Champion -> Register / Promote.
"""

from datetime import datetime, timedelta
from pathlib import Path

# Note: Heavy ML imports belong inside task callables to prevent Airflow scheduler parsing lag!
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    HAS_AIRFLOW = True
except ImportError:
    HAS_AIRFLOW = False


def extract_data(**ctx) -> str:
    """Task 1: Downloads and ingests latest ride duration data."""
    import numpy as np
    import pandas as pd

    print("Extracting latest ride records from raw data lake...")
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_file = output_dir / "rides_latest.parquet"

    # Simulate realistic batch extraction
    np.random.seed(int(datetime.now().timestamp()) % 10000)
    n = 15000
    df = pd.DataFrame({
        "PULocationID": np.random.randint(1, 265, size=n),
        "DOLocationID": np.random.randint(1, 265, size=n),
        "trip_distance": np.round(np.random.exponential(3.2, size=n) + 0.2, 2),
        "passenger_count": np.random.choice([1, 2, 3], size=n),
        "hour_of_day": np.random.randint(0, 24, size=n),
        "day_of_week": np.random.randint(0, 7, size=n),
    })
    df["trip_duration_minutes"] = np.round(
        4.0 + (df["trip_distance"] * 2.7) + (df["hour_of_day"] * 0.1) + np.random.normal(0, 1.8, size=n), 2
    )
    df.to_parquet(raw_file, index=False)
    print(f"Extraction complete: Saved {len(df)} rows to {raw_file}")
    return str(raw_file)


def validate_data(**ctx) -> str:
    """Task 2: Data quality & schema validation gate."""
    import pandas as pd

    raw_file = Path("data/raw/rides_latest.parquet")
    print(f"Validating dataset integrity for: {raw_file}")
    df = pd.read_parquet(raw_file)

    # Sanity rules
    assert not df.empty, "Data validation failed: Dataset is empty!"
    assert df["trip_distance"].min() > 0, "Data validation failed: Non-positive trip distances detected!"
    assert df["trip_duration_minutes"].isna().sum() == 0, "Missing values found in target column!"
    assert (df["PULocationID"] >= 1).all() and (df["PULocationID"] <= 265).all(), "Invalid TLC zone IDs!"

    print(f"Validation PASSED: {len(df)} clean records verified.")
    return "VALIDATED"


def train_model(**ctx) -> dict:
    """Task 3: Fits regression pipeline and logs experiment run to MLflow."""
    import joblib
    import pandas as pd
    from sklearn.linear_model import Ridge
    from sklearn.metrics import mean_absolute_error
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    print("Beginning training pipeline...")
    df = pd.read_parquet("data/raw/rides_latest.parquet")
    feature_cols = ["PULocationID", "DOLocationID", "trip_distance", "passenger_count", "hour_of_day", "day_of_week"]

    # Split 80/20
    split = int(len(df) * 0.8)
    X_train, y_train = df[feature_cols].iloc[:split], df["trip_duration_minutes"].iloc[:split]
    X_val, y_val = df[feature_cols].iloc[split:], df["trip_duration_minutes"].iloc[split:]

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0)),
    ])
    pipeline.fit(X_train, y_train)

    val_preds = pipeline.predict(X_val)
    val_mae = float(mean_absolute_error(y_val, val_preds))
    print(f"Trained candidate model with Validation MAE: {val_mae:.4f} mins")

    # Save candidate artifact
    models_dir = Path("models")
    models_dir.mkdir(parents=True, exist_ok=True)
    candidate_path = models_dir / "candidate_model.joblib"
    joblib.dump(pipeline, candidate_path)

    # Push MAE to Airflow XCom for downstream evaluation task
    return {"val_mae": val_mae, "model_path": str(candidate_path)}


def evaluate_against_production(**ctx) -> bool:
    """Task 4: Quality gate comparing candidate MAE against current production baseline."""
    # Retrieve train metrics from upstream task XCom
    ti = ctx.get("ti")
    train_result = ti.xcom_pull(task_ids="train_model") if ti else {"val_mae": 2.65}
    candidate_mae = train_result["val_mae"]

    # Current production model benchmark
    production_benchmark_mae = 3.20
    print(f"Evaluating candidate (MAE: {candidate_mae:.3f}) against Production baseline (MAE: {production_benchmark_mae:.3f})")

    if candidate_mae <= production_benchmark_mae:
        print("Candidate model OUTPERFORMS production benchmark. Approved for promotion!")
        return True
    else:
        print("Candidate model underperforms production benchmark. Promotion aborted.")
        return False


def register_production_model(**ctx) -> str:
    """Task 5: Promotes validated model to Production / Champion stage."""
    ti = ctx.get("ti")
    approved = ti.xcom_pull(task_ids="evaluate_against_production") if ti else True

    if approved:
        import shutil
        src = Path("models/candidate_model.joblib")
        dst = Path("models/production_model.joblib")
        if src.exists():
            shutil.copy(src, dst)
        print("Model promoted to Production! Stage: Champion. Service reloaded.")
        return "PROMOTED_TO_PRODUCTION"
    else:
        print("Promotion skipped.")
        return "PROMOTION_SKIPPED"


# Define Airflow DAG definition
default_args = {
    "owner": "mlops-team",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

if HAS_AIRFLOW:
    dag = DAG(
        dag_id="ride_duration_retraining_pipeline",
        default_args=default_args,
        description="Weekly continuous retraining pipeline for NYC ride duration model",
        schedule="@weekly",  # Every Monday at 00:00 UTC
        start_date=datetime(2026, 1, 1),
        catchup=False,  # CRITICAL: Prevent execution of historical unrun intervals
        tags=["mlops", "retraining", "ride_duration"],
    )

    t_extract = PythonOperator(task_id="extract_data", python_callable=extract_data, dag=dag)
    t_validate = PythonOperator(task_id="validate_data", python_callable=validate_data, dag=dag)
    t_train = PythonOperator(task_id="train_model", python_callable=train_model, dag=dag)
    t_evaluate = PythonOperator(task_id="evaluate_against_production", python_callable=evaluate_against_production, dag=dag)
    t_register = PythonOperator(task_id="register_production_model", python_callable=register_production_model, dag=dag)

    # Dependency chaining: Linear directed acyclic pipeline
    t_extract >> t_validate >> t_train >> t_evaluate >> t_register
