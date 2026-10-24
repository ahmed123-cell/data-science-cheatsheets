"""Machine Learning Model Wrapper and Inference Engine.

Implements clean OOP design pattern with an Abstract Base Class (ABC)
supporting interchangeable Scikit-Learn and ONNX Runtime inference engines.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
import numpy as np

try:
    import joblib
except ImportError:
    joblib = None

try:
    import onnxruntime as ort
except ImportError:
    ort = None

from src.logger import logger
from src.schemas import PredictionRequest


class BaseModelWrapper(ABC):
    """Abstract interface defining required model methods for production serving."""

    def __init__(self, model_version: str = "v1.0.0") -> None:
        self.model_version = model_version
        self.is_loaded = False

    @abstractmethod
    def load(self, model_path: Path) -> None:
        """Load model weights/graph into memory."""
        pass

    @abstractmethod
    def predict(self, request: PredictionRequest) -> float:
        """Preprocess request and return scalar predicted trip duration in minutes."""
        pass

    def preprocess(self, request: PredictionRequest) -> np.ndarray:
        """Transforms Pydantic request attributes into model input matrix.

        Feature Vector order:
        [PULocationID, DOLocationID, trip_distance, passenger_count, hour_of_day, day_of_week]
        """
        features = np.array(
            [
                [
                    float(request.PULocationID),
                    float(request.DOLocationID),
                    float(request.trip_distance),
                    float(request.passenger_count),
                    float(request.hour_of_day),
                    float(request.day_of_week),
                ]
            ],
            dtype=np.float32,
        )
        return features


class SklearnModelWrapper(BaseModelWrapper):
    """Scikit-Learn model wrapper loaded via joblib."""

    def __init__(self, model_version: str = "v1.0.0-sklearn") -> None:
        super().__init__(model_version)
        self.model: Any = None

    def load(self, model_path: Path) -> None:
        if model_path.exists() and joblib is not None:
            self.model = joblib.load(model_path)
            self.is_loaded = True
            logger.info("Loaded scikit-learn model from %s", model_path)
        else:
            # Fallback baseline model for immediate testing & container bootstrapping
            logger.warning(
                "Model file not found at %s. Bootstrapping heuristic baseline model.",
                model_path,
            )
            self._create_heuristic_baseline()

    def _create_heuristic_baseline(self) -> None:
        """Simple baseline: duration = 5.0 + (distance * 2.5) + (hour * 0.1)"""
        self.is_loaded = True
        self.model = "baseline"

    def predict(self, request: PredictionRequest) -> float:
        if not self.is_loaded:
            raise RuntimeError("Model is not loaded. Call load() first.")

        X = self.preprocess(request)
        if self.model == "baseline":
            # Heuristic calculation
            distance = request.trip_distance
            hour = request.hour_of_day
            duration = 5.0 + (distance * 2.5) + (hour * 0.15)
            return float(round(duration, 2))

        pred = self.model.predict(X)[0]
        # Durations must be strictly positive
        return float(round(max(1.0, float(pred)), 2))


class ONNXModelWrapper(BaseModelWrapper):
    """High-performance ONNX Runtime inference engine."""

    def __init__(self, model_version: str = "v1.0.0-onnx") -> None:
        super().__init__(model_version)
        self.session: Any = None
        self.input_name: str = ""

    def load(self, model_path: Path) -> None:
        if ort is not None and model_path.exists():
            opts = ort.SessionOptions()
            opts.graph_optimization_level = (
                ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            )
            self.session = ort.InferenceSession(
                str(model_path), sess_options=opts, providers=["CPUExecutionProvider"]
            )
            self.input_name = self.session.get_inputs()[0].name
            self.is_loaded = True
            logger.info("Loaded ONNX runtime session from %s", model_path)
        else:
            logger.warning(
                "ONNX model file %s not found. Falling back to heuristic baseline.",
                model_path,
            )
            self.is_loaded = True
            self.session = "baseline"

    def predict(self, request: PredictionRequest) -> float:
        if not self.is_loaded:
            raise RuntimeError("ONNX Session is not loaded. Call load() first.")

        if self.session == "baseline":
            duration = 5.0 + (request.trip_distance * 2.5) + (request.hour_of_day * 0.15)
            return float(round(duration, 2))

        X = self.preprocess(request)
        outputs = self.session.run(None, {self.input_name: X})
        raw_pred = outputs[0][0]
        if isinstance(raw_pred, (list, np.ndarray)):
            raw_pred = raw_pred[0]
        return float(round(max(1.0, float(raw_pred)), 2))
