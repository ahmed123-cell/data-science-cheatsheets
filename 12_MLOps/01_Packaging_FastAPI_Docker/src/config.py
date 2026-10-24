"""Application Configuration Module.

Loads configuration from environment variables with strong typing and default fallbacks.
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Central configuration for the MLOps inference application."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Service info
    APP_NAME: str = "ride-duration-inference-service"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "production"
    DEBUG: bool = False

    # Server binding
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Model configuration
    MODEL_BACKEND: str = "sklearn"  # options: "sklearn" | "onnx"
    MODEL_PATH: Path = Path("models/ride_duration_model.joblib")
    ONNX_MODEL_PATH: Path = Path("models/ride_duration_model.onnx")

    # Observability & thresholds
    LOG_LEVEL: str = "INFO"
    MAX_TRIP_DISTANCE_MILES: float = 100.0
    MIN_TRIP_DISTANCE_MILES: float = 0.1


# Singleton instance
settings = AppSettings()
