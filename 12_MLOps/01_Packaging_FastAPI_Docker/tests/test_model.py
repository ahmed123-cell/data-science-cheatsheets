"""Unit Tests for Model Preprocessing and Wrapper Interface."""

import numpy as np
from src.model import SklearnModelWrapper
from src.schemas import PredictionRequest


def test_model_preprocess_shape(valid_request_obj: PredictionRequest, model_wrapper: SklearnModelWrapper):
    """Verify preprocessing transforms Pydantic schema to (1, 6) numpy float32 matrix."""
    matrix = model_wrapper.preprocess(valid_request_obj)
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (1, 6)
    assert matrix.dtype == np.float32
    assert matrix[0, 2] == valid_request_obj.trip_distance


def test_model_predict_returns_positive_scalar(valid_request_obj: PredictionRequest, model_wrapper: SklearnModelWrapper):
    """Verify predict returns positive float duration in minutes."""
    prediction = model_wrapper.predict(valid_request_obj)
    assert isinstance(prediction, float)
    assert prediction >= 1.0


def test_unloaded_model_raises_runtime_error(valid_request_obj: PredictionRequest):
    """Verify calling predict on an unloaded wrapper raises RuntimeError."""
    empty_wrapper = SklearnModelWrapper()
    assert not empty_wrapper.is_loaded
    import pytest
    with pytest.raises(RuntimeError):
        empty_wrapper.predict(valid_request_obj)
