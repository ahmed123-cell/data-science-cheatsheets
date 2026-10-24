"""Integration and Endpoint Tests for FastAPI Inference Service."""

from fastapi.testclient import TestClient


def test_healthcheck_endpoint(client: TestClient):
    """Ensure /health returns 200 OK and model status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] in ["healthy", "degraded"]
    assert "version" in data
    assert "model_version" in data


def test_predict_endpoint_valid_payload(client: TestClient, valid_payload: dict):
    """Ensure /predict returns 200 with valid prediction payload."""
    response = client.post("/predict", json=valid_payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction_id" in data
    assert "predicted_duration_minutes" in data
    assert data["predicted_duration_minutes"] > 0.0
    assert "latency_ms" in data
    assert "model_version" in data
    # Ensure correlation ID header is propagated
    assert "X-Request-ID" in response.headers
    assert "X-Process-Time-Ms" in response.headers


def test_predict_endpoint_invalid_location_422(client: TestClient, valid_payload: dict):
    """Ensure /predict validates TLC location bounds (1 to 265) and returns 422 Unprocessable Entity."""
    bad_payload = valid_payload.copy()
    bad_payload["pickup_location_id"] = 9999  # Out of range!
    response = client.post("/predict", json=bad_payload)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


def test_predict_endpoint_negative_distance_422(client: TestClient, valid_payload: dict):
    """Ensure /predict rejects zero or negative trip distances."""
    bad_payload = valid_payload.copy()
    bad_payload["trip_distance"] = -5.0
    response = client.post("/predict", json=bad_payload)
    assert response.status_code == 422


def test_feedback_endpoint(client: TestClient):
    """Ensure /feedback records user actual trip duration."""
    feedback_payload = {
        "prediction_id": "c9bf9e57-1685-4c89-bafb-ff5af830be8a",
        "actual_duration_minutes": 14.5,
        "rating": 5,
    }
    response = client.post("/feedback", json=feedback_payload)
    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "accepted"
