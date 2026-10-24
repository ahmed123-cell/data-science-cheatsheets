"""Unit and Integration Tests for Orchestration and Serving Patterns."""

from pathlib import Path
from dags.ride_duration_retraining_dag import (
    evaluate_against_production,
    extract_data,
    train_model,
    validate_data,
)
from release_strategies.ab_testing_router import ABTestRouter
from release_strategies.blue_green_deploy import BlueGreenRouter


def test_airflow_dag_callables():
    """Validates that Airflow DAG extraction, validation, and training execute cleanly."""
    raw_path = extract_data()
    assert Path(raw_path).exists()

    val_status = validate_data()
    assert val_status == "VALIDATED"

    train_res = train_model()
    assert "val_mae" in train_res
    assert train_res["val_mae"] > 0.0

    eval_pass = evaluate_against_production()
    assert isinstance(eval_pass, bool)


def test_ab_test_router_determinism():
    """Ensures A/B routing yields deterministic assignments per user."""
    router = ABTestRouter(split_ratio=0.5)
    u = "user_42"
    assignment_1 = router.route_user(u)
    assignment_2 = router.route_user(u)
    assert assignment_1 == assignment_2
    assert assignment_1 in ["model_a_control", "model_b_challenger"]


def test_blue_green_router(tmp_path: Path):
    """Ensures Blue/Green router alternates targets properly."""
    config_file = tmp_path / "router.json"
    router = BlueGreenRouter(config_path=config_file)
    initial_color = router.get_active_target()

    new_color = router.flip()
    switched_target = router.get_active_target()
    assert new_color != initial_color
    assert switched_target["url"] != initial_color["url"]
