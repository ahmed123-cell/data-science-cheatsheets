"""BentoML Model Serving with Adaptive Micro-Batching (service.py).

Fixes FastAPI high-concurrency bottlenecks by aggregating individual incoming HTTP requests
into optimized vectorized micro-batches before passing to the model.
"""

from typing import Any
import numpy as np
from pydantic import BaseModel, Field

try:
    import bentoml
    HAS_BENTOML = True
except ImportError:
    HAS_BENTOML = False


class RideInput(BaseModel):
    PULocationID: int = Field(ge=1, le=265)
    DOLocationID: int = Field(ge=1, le=265)
    trip_distance: float = Field(gt=0.0)
    passenger_count: int = Field(default=1, ge=1, le=8)
    hour_of_day: int = Field(default=12, ge=0, le=23)
    day_of_week: int = Field(default=0, ge=0, le=6)


class RideOutput(BaseModel):
    predicted_duration_minutes: float
    model_version: str = "bentoml-v1"


# Dummy model for standalone execution
class ModelRunner:
    def predict_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        # Vectorized batch prediction: 5.0 + distance * 2.5 + hour * 0.15
        distances = batch_matrix[:, 2]
        hours = batch_matrix[:, 4]
        return np.round(5.0 + (distances * 2.5) + (hours * 0.15), 2)


runner = ModelRunner()


if HAS_BENTOML:
    @bentoml.service(
        name="ride_duration_bentoml_service",
        resources={"cpu": "2"},
    )
    class RideDurationService:
        """Production BentoML service with micro-batching."""

        @bentoml.api(batchable=True, batch_dim=0, max_batch_size=32, max_latency_ms=10)
        def predict(self, requests: list[RideInput]) -> list[RideOutput]:
            """Adaptive micro-batching endpoint.

            BentoML automatically queues concurrent user requests up to max_batch_size (32)
            or max_latency_ms (10ms) and invokes this function with the batched array.
            """
            features = np.array([
                [
                    float(r.PULocationID),
                    float(r.DOLocationID),
                    float(r.trip_distance),
                    float(r.passenger_count),
                    float(r.hour_of_day),
                    float(r.day_of_week),
                ]
                for r in requests
            ], dtype=np.float32)

            batch_predictions = runner.predict_batch(features)
            return [
                RideOutput(predicted_duration_minutes=float(pred))
                for pred in batch_predictions
            ]


def local_test_inference():
    """Local simulation testing adaptive micro-batching logic."""
    print("Testing BentoML micro-batching runner locally...")
    sample_inputs = [
        RideInput(PULocationID=10, DOLocationID=50, trip_distance=2.5, hour_of_day=8),
        RideInput(PULocationID=100, DOLocationID=150, trip_distance=12.0, hour_of_day=17),
        RideInput(PULocationID=43, DOLocationID=142, trip_distance=4.2, hour_of_day=12),
    ]
    matrix = np.array([
        [r.PULocationID, r.DOLocationID, r.trip_distance, r.passenger_count, r.hour_of_day, r.day_of_week]
        for r in sample_inputs
    ], dtype=np.float32)

    preds = runner.predict_batch(matrix)
    print("Vectorized Batch Outputs:", preds)
    for inp, out in zip(sample_inputs, preds):
        print(f"  Distance: {inp.trip_distance} mi, Hour: {inp.hour_of_day:02d}:00 -> Predicted: {out} mins")


if __name__ == "__main__":
    local_test_inference()
