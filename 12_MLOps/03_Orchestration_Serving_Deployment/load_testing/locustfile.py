"""Locust Load Testing Scenario for ML Inference Services (locustfile.py).

Simulates concurrent user traffic ramping to 100+ users to measure:
- Latency percentiles: p50, p95, p99
- Throughput: Requests Per Second (RPS)
- Failure / Error Rate (%)
"""

import random
from locust import HttpUser, between, task


class MLInferenceUser(HttpUser):
    """Simulated client issuing ride duration prediction requests."""

    # Wait between 0.5 and 2.0 seconds between tasks
    wait_time = between(0.5, 2.0)

    @task(5)
    def predict_ride_duration(self):
        """Simulates typical /predict request with realistic feature values."""
        payload = {
            "pickup_location_id": random.randint(1, 265),
            "dropoff_location_id": random.randint(1, 265),
            "trip_distance": round(random.uniform(0.5, 25.0), 2),
            "passenger_count": random.choice([1, 1, 1, 2, 3]),
            "hour_of_day": random.randint(0, 23),
            "day_of_week": random.randint(0, 6),
        }
        with self.client.post("/predict", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status code {response.status_code}: {response.text}")

    @task(1)
    def check_health(self):
        """Simulates periodic Kubernetes liveness/readiness probe."""
        self.client.get("/health")
