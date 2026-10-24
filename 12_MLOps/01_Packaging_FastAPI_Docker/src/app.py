"""Production FastAPI ML Inference Application.

Implements lifespan resource management, correlation ID middleware,
structured JSON logging, and strict Pydantic boundary validation.
"""

import time
import uuid
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import settings
from src.logger import logger, set_request_id
from src.model import BaseModelWrapper, ONNXModelWrapper, SklearnModelWrapper
from src.schemas import (
    FeedbackRequest,
    HealthResponse,
    PredictionRequest,
    PredictionResponse,
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan context manager: loads model at startup, cleans up on shutdown."""
    logger.info("Initializing ML inference application...")

    # Choose inference backend
    if settings.MODEL_BACKEND == "onnx":
        wrapper: BaseModelWrapper = ONNXModelWrapper()
        wrapper.load(settings.ONNX_MODEL_PATH)
    else:
        wrapper = SklearnModelWrapper()
        wrapper.load(settings.MODEL_PATH)

    app.state.model = wrapper
    logger.info(
        "Model successfully initialized with backend: %s (version: %s)",
        settings.MODEL_BACKEND,
        wrapper.model_version,
    )

    yield

    logger.info("Shutting down ML inference application. Releasing resources...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production REST API serving Ride Duration predictions with full observability.",
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def correlation_and_timing_middleware(
    request: Request, call_next
) -> Response:
    """Attaches unique X-Request-ID and measures request latency for structured logs."""
    req_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    set_request_id(req_id)
    start_time = time.perf_counter()

    try:
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start_time) * 1000.0
        response.headers["X-Request-ID"] = req_id
        response.headers["X-Process-Time-Ms"] = f"{duration_ms:.2f}"

        logger.info(
            "HTTP request completed",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "latency_ms": round(duration_ms, 2),
            },
        )
        return response
    except Exception as exc:
        duration_ms = (time.perf_counter() - start_time) * 1000.0
        logger.error(
            "Unhandled server error occurred: %s",
            str(exc),
            exc_info=True,
            extra={
                "method": request.method,
                "path": request.url.path,
                "latency_ms": round(duration_ms, 2),
            },
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal server error", "request_id": req_id},
        )


@app.get("/health", response_model=HealthResponse, tags=["Observability"])
async def healthcheck() -> HealthResponse:
    """Service health and model readiness probe."""
    model: BaseModelWrapper = getattr(app.state, "model", None)
    is_ready = model is not None and model.is_loaded

    return HealthResponse(
        status="healthy" if is_ready else "degraded",
        model_loaded=is_ready,
        model_version=model.model_version if model else "unloaded",
        version=settings.APP_VERSION,
    )


@app.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK,
    tags=["Inference"],
)
async def predict_ride_duration(payload: PredictionRequest) -> PredictionResponse:
    """Computes predicted taxi ride duration in minutes."""
    model: BaseModelWrapper = getattr(app.state, "model", None)
    if not model or not model.is_loaded:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not ready for inference.",
        )

    start_calc = time.perf_counter()
    predicted_val = model.predict(payload)
    compute_latency_ms = (time.perf_counter() - start_calc) * 1000.0

    prediction_id = str(uuid.uuid4())
    logger.info(
        "Prediction generated successfully",
        extra={
            "prediction_id": prediction_id,
            "predicted_duration": predicted_val,
            "trip_distance": payload.trip_distance,
            "model_latency_ms": round(compute_latency_ms, 3),
        },
    )

    return PredictionResponse(
        prediction_id=prediction_id,
        predicted_duration_minutes=predicted_val,
        model_version=model.model_version,
        model_backend=settings.MODEL_BACKEND,
        latency_ms=round(compute_latency_ms, 3),
    )


@app.post("/feedback", status_code=status.HTTP_202_ACCEPTED, tags=["Feedback"])
async def submit_feedback(feedback: FeedbackRequest) -> dict[str, str]:
    """Ingests ground truth ride duration to power drift monitoring and model evaluation."""
    logger.info(
        "Feedback ground truth received",
        extra={
            "prediction_id": feedback.prediction_id,
            "actual_duration": feedback.actual_duration_minutes,
            "rating": feedback.rating,
        },
    )
    return {
        "status": "accepted",
        "message": f"Feedback recorded for prediction {feedback.prediction_id}",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
