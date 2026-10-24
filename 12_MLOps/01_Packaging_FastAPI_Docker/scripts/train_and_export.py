"""Training and Multi-Format Model Export Script.

Trains a scikit-learn regression model on ride duration data and exports it to:
1. Joblib (.joblib) for standard Python runtime
2. ONNX (.onnx) for C++ / high-throughput accelerated runtime
"""

from pathlib import Path
import joblib
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

try:
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType
    HAS_SKL2ONNX = True
except ImportError:
    HAS_SKL2ONNX = False


def generate_synthetic_ride_data(n_samples: int = 5000, random_seed: int = 42):
    """Generates synthetic NYC ride data resembling NYC Green/Yellow taxi trips."""
    np.random.seed(random_seed)
    pu = np.random.randint(1, 265, size=n_samples)
    do = np.random.randint(1, 265, size=n_samples)
    distance = np.random.exponential(scale=3.5, size=n_samples) + 0.2
    distance = np.clip(distance, 0.2, 50.0)
    passenger = np.random.choice([1, 2, 3, 4, 5], p=[0.7, 0.15, 0.08, 0.04, 0.03], size=n_samples)
    hour = np.random.randint(0, 24, size=n_samples)
    dow = np.random.randint(0, 7, size=n_samples)

    # Realistic duration equation with noise
    rush_hour_multiplier = np.where((hour >= 7) & (hour <= 9) | (hour >= 17) & (hour <= 19), 1.35, 1.0)
    duration = (4.0 + (distance * 2.8 * rush_hour_multiplier) + (hour * 0.1) + np.random.normal(0, 2.0, size=n_samples))
    duration = np.clip(duration, 2.0, 120.0)

    X = np.column_stack([pu, do, distance, passenger, hour, dow]).astype(np.float32)
    y = duration.astype(np.float32)
    return X, y


def train_and_export():
    """Trains model, logs metrics, and exports weights."""
    print("Generating training dataset...")
    X_train, y_train = generate_synthetic_ride_data(n_samples=10000, random_seed=42)
    X_val, y_val = generate_synthetic_ride_data(n_samples=2000, random_seed=99)

    print("Fitting Ridge regression pipeline...")
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0)),
    ])
    pipeline.fit(X_train, y_train)

    val_preds = pipeline.predict(X_val)
    mae = mean_absolute_error(y_val, val_preds)
    rmse = root_mean_squared_error(y_val, val_preds)
    print(f"Validation Metrics -> MAE: {mae:.2f} mins | RMSE: {rmse:.2f} mins")

    # Save to models directory
    models_dir = Path("models")
    models_dir.mkdir(parents=True, exist_ok=True)

    joblib_path = models_dir / "ride_duration_model.joblib"
    joblib.dump(pipeline, joblib_path)
    print(f"Exported Scikit-Learn model to: {joblib_path}")

    # Export to ONNX if skl2onnx is installed
    onnx_path = models_dir / "ride_duration_model.onnx"
    if HAS_SKL2ONNX:
        initial_type = [("float_input", FloatTensorType([None, 6]))]
        onnx_model = convert_sklearn(pipeline, initial_types=initial_type, target_opset=15)
        with open(onnx_path, "wb") as f:
            f.write(onnx_model.SerializeToString())
        print(f"Exported ONNX model to: {onnx_path}")
    else:
        print("Note: skl2onnx not installed in current environment. Install with: pip install skl2onnx")


if __name__ == "__main__":
    train_and_export()
