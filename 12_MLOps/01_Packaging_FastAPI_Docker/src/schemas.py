"""Pydantic V2 Data Validation Schemas for ML Inference API.

Enforces strict boundary contracts on all inbound requests and outbound responses.
"""

from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict


class PredictionRequest(BaseModel):
    """Input payload representing ride features required for trip duration prediction."""

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "PULocationID": 43,
                "DOLocationID": 142,
                "trip_distance": 3.75,
                "passenger_count": 1,
                "hour_of_day": 14,
                "day_of_week": 2,
            }
        },
    )

    PULocationID: Annotated[
        int,
        Field(
            ge=1,
            le=265,
            description="TLC Taxi Zone Pick-Up location ID (1 to 265)",
            alias="pickup_location_id",
        ),
    ]
    DOLocationID: Annotated[
        int,
        Field(
            ge=1,
            le=265,
            description="TLC Taxi Zone Drop-Off location ID (1 to 265)",
            alias="dropoff_location_id",
        ),
    ]
    trip_distance: Annotated[
        float,
        Field(
            gt=0.0,
            le=150.0,
            description="Estimated trip distance in miles",
        ),
    ]
    passenger_count: Annotated[
        int,
        Field(
            ge=1,
            le=8,
            default=1,
            description="Number of passengers in the vehicle",
        ),
    ]
    hour_of_day: Annotated[
        int,
        Field(
            ge=0,
            le=23,
            default=12,
            description="Hour of day (0-23 in 24h format)",
        ),
    ]
    day_of_week: Annotated[
        int,
        Field(
            ge=0,
            le=6,
            default=0,
            description="Day of week (0=Monday, 6=Sunday)",
        ),
    ]


class PredictionResponse(BaseModel):
    """Prediction result returned to the client."""

    prediction_id: str = Field(description="Unique UUID for this prediction event")
    predicted_duration_minutes: float = Field(
        description="Predicted ride duration in minutes"
    )
    model_version: str = Field(description="Version tag of the active serving model")
    model_backend: str = Field(description="Inference backend: sklearn or onnx")
    latency_ms: float = Field(description="Model compute latency in milliseconds")


class HealthResponse(BaseModel):
    """Healthcheck and readiness response."""

    status: str = Field(default="healthy", description="Service status: healthy | degraded")
    model_loaded: bool = Field(description="Whether the ML inference model is loaded in memory")
    model_version: str = Field(description="Active model version")
    version: str = Field(description="Application API semantic version")


class FeedbackRequest(BaseModel):
    """Feedback payload pairing prediction ID with true actual ride duration."""

    prediction_id: str = Field(description="UUID of the original prediction")
    actual_duration_minutes: float = Field(
        gt=0.0,
        description="Ground truth actual duration observed after trip completion",
    )
    rating: int | None = Field(
        default=None,
        ge=1,
        le=5,
        description="Optional customer satisfaction rating (1-5)",
    )
