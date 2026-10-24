"""Unit Tests for Drift Detection and RAGAS Metrics."""

import numpy as np
from drift_detection.statistical_drift_tests import (
    calculate_psi,
    chi_square_test,
    kolmogorov_smirnov_test,
    wasserstein_distance_test,
)
from rag_evaluation_ragas.ragas_evaluator import RAGASEvaluationSuite


def test_psi_identical_distributions():
    """Identical distributions must yield a negligible PSI < 0.05."""
    np.random.seed(42)
    sample = np.random.normal(loc=10.0, scale=2.0, size=2000)
    result = calculate_psi(sample, sample)
    assert result["psi"] < 0.05
    assert result["drift_level"] == "NO_DRIFT"


def test_psi_shifted_distribution():
    """Significantly shifted distribution must yield high PSI > 0.15."""
    np.random.seed(42)
    baseline = np.random.normal(loc=10.0, scale=2.0, size=2000)
    drifted = np.random.normal(loc=14.0, scale=2.0, size=2000)
    result = calculate_psi(baseline, drifted)
    assert result["psi"] > 0.15
    assert result["drift_level"] in ["MODERATE_DRIFT", "SIGNIFICANT_DRIFT"]


def test_ks_test_detects_drift():
    """KS test must reject null hypothesis for shifted samples."""
    np.random.seed(42)
    a = np.random.exponential(scale=2.0, size=1000)
    b = np.random.exponential(scale=5.0, size=1000)
    res = kolmogorov_smirnov_test(a, b)
    assert res["drift_detected"] is True
    assert res["p_value"] < 0.05


def test_chi_square_categorical():
    """Chi-square detects frequency shift in categories."""
    ref = ["A"] * 500 + ["B"] * 500
    curr = ["A"] * 800 + ["B"] * 200
    res = chi_square_test(ref, curr)
    assert res["drift_detected"] is True
    assert res["p_value"] < 0.001


def test_wasserstein_distance():
    """Wasserstein distance matches physical shift magnitude."""
    a = np.ones(500) * 5.0
    b = np.ones(500) * 8.0
    res = wasserstein_distance_test(a, b)
    assert abs(res["wasserstein_distance"] - 3.0) < 0.01


def test_ragas_metrics():
    """RAGAS evaluator produces valid normalized scores."""
    evaluator = RAGASEvaluationSuite()
    sample = {
        "question": "What is the fee?",
        "ground_truth_facts": ["The airport fee is $1.75."],
        "retrieved_contexts": ["The airport access fee is $1.75."],
        "ranked_chunks": [{"chunk_id": "1", "is_relevant": True}],
        "answer_claims": ["The fee is $1.75."],
    }
    scores = evaluator.evaluate_sample(sample)
    assert 0.0 <= scores["faithfulness"] <= 1.0
    assert 0.0 <= scores["context_precision"] <= 1.0
    assert 0.0 <= scores["context_recall"] <= 1.0
    assert scores["faithfulness"] == 1.0
    assert scores["context_recall"] == 1.0
