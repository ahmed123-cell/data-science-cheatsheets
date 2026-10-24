"""Weights & Biases (W&B) Experiment Tracking and Hyperparameter Sweeps (train_wandb.py).

Demonstrates cloud-native experiment tracking, artifact versioning, and sweep definitions.
"""

import numpy as np

try:
    import wandb
    HAS_WANDB = True
except ImportError:
    HAS_WANDB = False


SWEEP_CONFIGURATION = {
    "method": "bayes",  # Bayesian hyperparameter optimization
    "metric": {
        "name": "val_mae",
        "goal": "minimize",
    },
    "parameters": {
        "alpha": {
            "distribution": "uniform",
            "min": 0.01,
            "max": 10.0,
        },
        "model_type": {
            "values": ["ridge", "lasso"],
        },
        "fit_intercept": {
            "values": [True, False],
        },
    },
}


def run_wandb_training_session(config=None):
    """Executes a single W&B training run."""
    if not HAS_WANDB:
        print("wandb is not installed. Run 'pip install wandb' to enable W&B tracking.")
        return

    with wandb.init(config=config, project="nyc-ride-duration", entity="mlops-team") as run:
        cfg = wandb.config

        # Simulated training loop logging metrics per epoch
        print(f"Executing W&B Run with alpha={cfg.get('alpha', 1.0)}")
        for epoch in range(1, 10):
            simulated_train_loss = 5.0 / (epoch + 0.5) + np.random.uniform(0, 0.2)
            simulated_val_mae = 3.2 + (1.0 / epoch) + np.random.uniform(0, 0.1)

            # Log step metrics to W&B cloud dashboard
            wandb.log({
                "epoch": epoch,
                "train_loss": simulated_train_loss,
                "val_mae": simulated_val_mae,
            })

        # Log Model Artifact with lineage
        artifact = wandb.Artifact("ride-regressor", type="model", description="Trained ride duration regressor")
        # In production: artifact.add_file("models/pipeline.joblib")
        run.log_artifact(artifact)
        print("Run logged successfully to Weights & Biases.")


if __name__ == "__main__":
    run_wandb_training_session()
