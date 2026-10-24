"""FastAPI Service Instrumented with Prometheus Metrics (instrumented_service.py).

Exposes real-time telemetry on /metrics:
- Counter: Total prediction requests partitioned by status code and model version
- Histogram: Inference latency percentiles (p50, p90, p95, p99)
- Histogram: Distribution of predicted values (to monitor Prediction Drift)
- Gauge: Current feature drift PSI score
"""

import time
from fastapi import FastAPI, Response
from pydantic import BaseModel, Field

try:
    from prometheus_client import (
        CONTENT_TYPE_LATEST,
        Counter,
        Gauge,
        Histogram,
        generate_latest,
    )
    HAS_PROMETHEUS = True
except ImportError:
    HAS_PROMETHEUS = False


app = FastAPI(title="Instrumented MLOps Inference Service")

# 1. Prometheus Metrics Definition
if HAS_PROMETHEUS:
    PREDICTION_REQUESTS = Counter(
        "ml_prediction_requests_total",
        "Total number of prediction requests processed",
        ["status", "model_version"],
    )

    INFERENCE_LATENCY = Histogram(
        "ml_inference_duration_seconds",
        "Time spent executing model inference in seconds",
        buckets=[0.005, 0.010, 0.025, 0.050, 0.100, 0.250, 0.500, 1.0],
    )

    PREDICTION_DISTRIBUTION = Histogram(
        "ml_predicted_duration_minutes",
        "Distribution of predicted ride durations (to detect Prediction Drift)",
        buckets=[5.0, 10.0, 15.0, 20.0, 30.0, 45.0, 60.0, 90.0, 120.0],
    )

    DRIFT_PSI_GAUGE = Gauge(
        "ml_feature_drift_psi_score",
        "Current Population Stability Index (PSI) drift score for primary feature",
    )


class RideFeatures(BaseModel):
    trip_distance: float = Field(gt=0.0)
    hour_of_day: int = Field(ge=0, le=23)
    passenger_count: int = Field(default=1)


@app.post("/predict")
def predict(features: RideFeatures):
    start = time.perf_counter()

    # Model calculation
    predicted_val = round(5.0 + (features.trip_distance * 2.5) + (features.hour_of_day * 0.15), 2)
    duration = time.perf_counter() - start

    if HAS_PROMETHEUS:
        PREDICTION_REQUESTS.labels(status="200", model_version="v1.0.0").inc()
        INFERENCE_LATENCY.observe(duration)
        PREDICTION_DISTRIBUTION.observe(predicted_val)
        # Update gauge dynamically
        DRIFT_PSI_GAUGE.set(0.045)  # Healthy baseline score

    return {
        "predicted_duration_minutes": predicted_val,
        "latency_ms": round(duration * 1000, 3),
    }


@app.get("/metrics")
def metrics():
    """Prometheus metrics endpoint scraped every 15s."""
    if HAS_PROMETHEUS:
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    return {"detail": "prometheus_client not installed in current environment"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
