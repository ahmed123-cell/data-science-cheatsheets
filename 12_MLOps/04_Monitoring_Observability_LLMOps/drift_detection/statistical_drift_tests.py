"""Statistical Tests for Data and Prediction Drift Detection.

Implements the four foundational statistical tests for MLOps monitoring:
1. Population Stability Index (PSI) - Continuous/Binned
2. Two-Sample Kolmogorov-Smirnov (KS) Test - Continuous non-parametric
3. Chi-Square Goodness-of-Fit Test - Categorical features
4. Wasserstein Distance (Earth Mover's Distance) - Distribution shift distance
"""

from typing import Any
import numpy as np
from scipy import stats


def calculate_psi(
    reference: np.ndarray,
    current: np.ndarray,
    num_buckets: int = 10,
    epsilon: float = 1e-4,
) -> dict[str, Any]:
    """Computes Population Stability Index (PSI) between baseline and production data.

    Formula:
        PSI = sum( (Actual_i - Expected_i) * ln(Actual_i / Expected_i) )

    Thresholds:
        PSI < 0.10: Stable, no significant shift.
        0.10 <= PSI < 0.20: Moderate shift; investigate features.
        PSI >= 0.20: Significant drift; trigger retraining alert.
    """
    reference = np.asarray(reference).ravel()
    current = np.asarray(current).ravel()

    # Determine quantile bins based on reference distribution
    percentiles = np.linspace(0, 100, num_buckets + 1)
    bins = np.percentile(reference, percentiles)
    bins[0] = -np.inf
    bins[-1] = np.inf

    # Calculate bucket counts
    expected_counts, _ = np.histogram(reference, bins=bins)
    actual_counts, _ = np.histogram(current, bins=bins)

    # Convert to proportions with smoothing epsilon to prevent division by zero
    expected_pct = (expected_counts / len(reference)) + epsilon
    actual_pct = (actual_counts / len(current)) + epsilon

    # Re-normalize to ensure sum to 1.0
    expected_pct /= np.sum(expected_pct)
    actual_pct /= np.sum(actual_pct)

    # Calculate PSI per bucket
    bucket_psi = (actual_pct - expected_pct) * np.log(actual_pct / expected_pct)
    total_psi = float(np.sum(bucket_psi))

    if total_psi < 0.10:
        drift_level = "NO_DRIFT"
        action = "Monitor normally."
    elif total_psi < 0.20:
        drift_level = "MODERATE_DRIFT"
        action = "Investigate feature distributions and prepare retraining pipeline."
    else:
        drift_level = "SIGNIFICANT_DRIFT"
        action = "TRIGGER ALERT: Automated retraining required or fallback to champion model."

    return {
        "psi": round(total_psi, 4),
        "drift_level": drift_level,
        "action_required": action,
        "num_buckets": num_buckets,
    }


def kolmogorov_smirnov_test(reference: np.ndarray, current: np.ndarray) -> dict[str, Any]:
    """Performs Two-Sample Kolmogorov-Smirnov (KS) test for continuous distributions.

    Tests null hypothesis H0: Both samples originate from the identical continuous distribution.
    Rejects H0 if p-value < 0.05.
    """
    res = stats.ks_2samp(reference, current)
    is_drifted = bool(res.pvalue < 0.05)
    return {
        "ks_statistic": round(float(res.statistic), 4),
        "p_value": float(res.pvalue),
        "drift_detected": is_drifted,
        "test_name": "Kolmogorov-Smirnov Two-Sample",
    }


def wasserstein_distance_test(reference: np.ndarray, current: np.ndarray) -> dict[str, Any]:
    """Computes Wasserstein Distance (Earth Mover's Distance) between two 1D distributions."""
    distance = stats.wasserstein_distance(reference, current)
    return {
        "wasserstein_distance": round(float(distance), 4),
        "test_name": "Wasserstein Earth Mover Distance",
    }


def chi_square_test(reference_categories: list[Any], current_categories: list[Any]) -> dict[str, Any]:
    """Chi-Square Goodness-of-Fit test for categorical features."""
    all_cats = sorted(list(set(reference_categories) | set(current_categories)))
    ref_counts = [reference_categories.count(c) for c in all_cats]
    curr_counts = [current_categories.count(c) for c in all_cats]

    # Convert to expected frequencies based on reference
    ref_total = sum(ref_counts)
    curr_total = sum(curr_counts)
    expected = [max(1e-3, (rc / ref_total) * curr_total) for rc in ref_counts]

    chi2_stat, p_val = stats.chisquare(f_obs=curr_counts, f_exp=expected)
    return {
        "chi2_statistic": round(float(chi2_stat), 4),
        "p_value": float(p_val),
        "drift_detected": bool(p_val < 0.05),
        "test_name": "Chi-Square Goodness-of-Fit",
    }


def demo_drift_detection():
    print("=" * 65)
    print("MLOps Statistical Drift Detection Demonstration")
    print("=" * 65)

    np.random.seed(42)
    # Reference baseline distribution (e.g. Training trip distance)
    baseline_distances = np.random.exponential(scale=3.5, size=2000)

    # Scenario A: In-distribution production data (No drift)
    in_dist_distances = np.random.exponential(scale=3.55, size=1500)

    # Scenario B: Shifted production data (Data Drift: longer airport trips)
    drifted_distances = np.random.exponential(scale=5.8, size=1500)

    print("\n--- Testing In-Distribution Production Traffic ---")
    psi_a = calculate_psi(baseline_distances, in_dist_distances)
    ks_a = kolmogorov_smirnov_test(baseline_distances, in_dist_distances)
    print(f"  PSI: {psi_a['psi']} -> Level: {psi_a['drift_level']}")
    print(f"  KS Test: p-value={ks_a['p_value']:.4f} -> Drift: {ks_a['drift_detected']}")

    print("\n--- Testing Shifted Production Traffic (Data Drift) ---")
    psi_b = calculate_psi(baseline_distances, drifted_distances)
    ks_b = kolmogorov_smirnov_test(baseline_distances, drifted_distances)
    print(f"  PSI: {psi_b['psi']} -> Level: {psi_b['drift_level']}")
    print(f"  Action: {psi_b['action_required']}")
    print(f"  KS Test: p-value={ks_b['p_value']:.4e} -> Drift: {ks_b['drift_detected']}")
    print("=" * 65)


if __name__ == "__main__":
    demo_drift_detection()
