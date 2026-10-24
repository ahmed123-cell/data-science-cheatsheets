"""Structured JSON Logging with Request Correlation IDs.

Ensures all application and inference logs output searchable, parsed JSON
compatible with Datadog, CloudWatch, ELK, and Grafana Loki.
"""

import json
import logging
import sys
import uuid
from contextvars import ContextVar
from datetime import datetime, timezone

# Context variable holding the correlation ID across async coroutine calls
request_id_ctx: ContextVar[str] = ContextVar("request_id", default="system")


def get_request_id() -> str:
    """Get the current request ID from context."""
    return request_id_ctx.get()


def set_request_id(req_id: str | None = None) -> str:
    """Set or generate a new request correlation ID."""
    rid = req_id or str(uuid.uuid4())
    request_id_ctx.set(rid)
    return rid


class JSONFormatter(logging.Formatter):
    """Custom JSON formatter outputting production-grade log payloads."""

    def format(self, record: logging.LogRecord) -> str:
        log_payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "request_id": get_request_id(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        # Include extra attributes attached to logger calls (e.g. latency_ms, endpoint)
        for key, value in record.__dict__.items():
            if key not in logging.LogRecord.__dict__ and key not in log_payload:
                log_payload[key] = value

        if record.exc_info:
            log_payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_payload)


def setup_logger(name: str = "mlops", log_level: str = "INFO") -> logging.Logger:
    """Initializes and returns a structured JSON logger."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level.upper())

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)

    logger.propagate = False
    return logger


logger = setup_logger()
