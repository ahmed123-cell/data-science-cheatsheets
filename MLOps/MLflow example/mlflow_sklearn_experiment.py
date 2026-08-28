"""
MLflow + scikit-learn Experiment Tracking Example

This script:
1. Loads a classic scikit-learn dataset (Breast Cancer)
2. Trains multiple models with different hyperparameters
3. Logs parameters, metrics, and models to MLflow
4. Compares results across runs

Usage:
    python mlflow_sklearn_experiment.py

Then open the MLflow UI:
    mlflow ui
    # Navigate to http://localhost:5000
"""

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

import pandas as pd
import numpy as np


# -------------------------------------------------
# 1. Configuration
# -------------------------------------------------
EXPERIMENT_NAME = "breast-cancer-classification"
RANDOM_STATE = 42
TEST_SIZE = 0.2


def load_and_prepare_data():
    """Load the Breast Cancer dataset and split into train/test."""
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    return X_train, X_test, y_train, y_test, data.feature_names


def evaluate_model(model, X_test, y_test):
    """Calculate common classification metrics."""
    y_pred = model.predict(X_test)
    y_proba = None

    # Some models support predict_proba
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
    }

    if y_proba is not None:
        metrics["roc_auc"] = roc_auc_score(y_test, y_proba)

    return metrics, y_pred


def train_and_log_model(name, model, params, X_train, X_test, y_train, y_test):
    """
    Train a model inside an MLflow run and log everything.
    """
    with mlflow.start_run(run_name=name):
        # Log hyperparameters
        mlflow.log_params(params)
        mlflow.log_param("model_type", name)

        # Create a pipeline with scaling (good practice)
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", model)
        ])

        # Train
        pipeline.fit(X_train, y_train)

        # Evaluate
        metrics, _ = evaluate_model(pipeline, X_test, y_test)

        # Log metrics
        mlflow.log_metrics(metrics)

        # Infer model signature (input/output schema)
        signature = infer_signature(X_train, pipeline.predict(X_train))

        # Log the model
        mlflow.sklearn.log_model(
            sk_model=pipeline,
            artifact_path="model",
            signature=signature,
            input_example=X_train.iloc[:5],
            registered_model_name=None,  # set a name if you want to register
        )

        # Print results
        print(f"\n{'='*50}")
        print(f"Model: {name}")
        print(f"{'='*50}")
        for metric, value in metrics.items():
            print(f"  {metric:12}: {value:.4f}")
        print(f"  Run ID     : {mlflow.active_run().info.run_id}")

        return metrics


def main():

    # Optional: set tracking URI (default is local ./mlruns)
    mlflow.set_tracking_uri("sqlite:///./mlflow.db")

    # Set experiment (creates it if it doesn't exist)
    mlflow.set_experiment(EXPERIMENT_NAME)



    print(f"Starting experiment: {EXPERIMENT_NAME}")
    print("-" * 60)

    # Load data
    X_train, X_test, y_train, y_test, feature_names = load_and_prepare_data()
    print(f"Dataset shape : {X_train.shape[0] + X_test.shape[0]} samples, {X_train.shape[1]} features")
    print(f"Train / Test  : {X_train.shape[0]} / {X_test.shape[0]}")

    # -------------------------------------------------
    # Define multiple models + hyperparameters
    # -------------------------------------------------
    models_to_train = [
        {
            "name": "LogisticRegression",
            "model": LogisticRegression(max_iter=1000, random_state=RANDOM_STATE),
            "params": {
                "C": 1.0,
                "solver": "lbfgs",
                "max_iter": 1000,
            },
        },
        {
            "name": "RandomForest",
            "model": RandomForestClassifier(random_state=RANDOM_STATE),
            "params": {
                "n_estimators": 100,
                "max_depth": 8,
                "min_samples_split": 5,
            },
        },
        {
            "name": "RandomForest",
            "model": RandomForestClassifier(random_state=RANDOM_STATE),
            "params": {
                "n_estimators": 300,
                "max_depth": 4,
                "min_samples_split": 3,
            },
        },
        {
            "name": "GradientBoosting",
            "model": GradientBoostingClassifier(random_state=RANDOM_STATE),
            "params": {
                "n_estimators": 100,
                "learning_rate": 0.1,
                "max_depth": 3,
            },
        },
        {
            "name": "SVM",
            "model": SVC(probability=True, random_state=RANDOM_STATE),
            "params": {
                "C": 1.0,
                "kernel": "rbf",
                "gamma": "scale",
            },
        },
        {
            "name": "KNN",
            "model": KNeighborsClassifier(),
            "params": {
                "n_neighbors": 5,
                "weights": "uniform",
                "metric": "minkowski",
            },
        },
    ]

    # -------------------------------------------------
    # Train all models and log to MLflow
    # -------------------------------------------------
    results = []
    for config in models_to_train:
        metrics = train_and_log_model(
            name=config["name"],
            model=config["model"],
            params=config["params"],
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test,
        )
        results.append({"model": config["name"], **metrics})

    # -------------------------------------------------
    # Summary table
    # -------------------------------------------------
    print("\n" + "=" * 60)
    print("SUMMARY - All Models Comparison")
    print("=" * 60)
    summary_df = pd.DataFrame(results).sort_values("f1", ascending=False)
    print(summary_df.to_string(index=False, float_format="%.4f"))
    print("\nBest model by F1-score:", summary_df.iloc[0]["model"])

    print("\n" + "-" * 60)
    print("Experiment finished!")
    print("Run the following command to open the MLflow UI:")
    print("    mlflow ui")
    print("Then go to: http://localhost:5000")
    print("-" * 60)


if __name__ == "__main__":
    main()
