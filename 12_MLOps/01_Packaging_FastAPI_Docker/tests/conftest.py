"""Pytest Fixtures and Global Test Configuration."""

import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.model import SklearnModelWrapper
from src.schemas import PredictionRequest


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Yields FastAPI TestClient instance for testing HTTP endpoints."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def valid_payload() -> dict:
    """Sample valid taxi trip feature payload."""
    return {
        "pickup_location_id": 43,
        "dropoff_location_id": 142,
        "trip_distance": 3.75,
        "passenger_count": 2,
        "hour_of_day": 14,
        "day_of_week": 2,
    }


@pytest.fixture
def valid_request_obj(valid_payload: dict) -> PredictionRequest:
    """Instantiated Pydantic PredictionRequest object."""
    return PredictionRequest(**valid_payload)


@pytest.fixture
def model_wrapper() -> SklearnModelWrapper:
    """Initialized heuristic baseline model wrapper."""
    wrapper = SklearnModelWrapper()
    wrapper._create_heuristic_baseline()
    return wrapper
