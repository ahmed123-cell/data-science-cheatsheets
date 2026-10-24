# ==============================================================================
# Multi-Stage Production Dockerfile for ML Inference Service
# Stage 1: Build & Dependency Wheel Compilation
# Stage 2: Lean Unprivileged Runtime Container
# ==============================================================================

# ----------------- Stage 1: Builder -----------------
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml to pre-build wheels
COPY pyproject.toml .

# Create virtual environment and compile wheels
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir .

# ----------------- Stage 2: Final Runtime -----------------
FROM python:3.11-slim AS runtime

# Set security environment flags
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH" \
    PORT=8000 \
    HOST=0.0.0.0

WORKDIR /app

# Create unprivileged system user for security compliance (non-root)
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /sbin/nologin -d /app appuser

# Copy installed virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application source code and models
COPY --chown=appuser:appgroup src/ /app/src/
COPY --chown=appuser:appgroup models/ /app/models/
COPY --chown=appuser:appgroup pyproject.toml /app/

# Switch to unprivileged non-root user
USER appuser

# Healthcheck probe to verify service readiness
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

EXPOSE 8000

# Run using production ASGI server uvicorn
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
