"""Inference Pattern 3: Streaming Event Consumer & Real-Time Scorer (consumer.py).

Consumes ride booking events from the event bus, runs sub-millisecond inference,
and emits prediction events to a downstream topic.
"""

import json
import time


def score_single_event(event: dict) -> dict:
    """Processes one streaming event and generates an enriched prediction payload."""
    ride_info = event["ride_info"]
    dist = ride_info["trip_distance"]
    hour = ride_info["hour_of_day"]

    # Low-latency heuristic / model inference
    predicted_duration = round(4.5 + (dist * 2.6) + (hour * 0.12), 2)

    return {
        "event_id": event["event_id"],
        "processed_at": time.time(),
        "predicted_duration_minutes": predicted_duration,
        "features": ride_info,
        "model_version": "streaming-regressor-v1",
    }


def simulate_event_consumer(events: list[dict]):
    """Demonstrates consumer loop over incoming message stream."""
    print("=" * 55)
    print("STREAMING INFERENCE CONSUMER RUNNING")
    print("=" * 55)

    latencies_ms = []
    for event in events:
        t0 = time.perf_counter()
        prediction_payload = score_single_event(event)
        latency_ms = (time.perf_counter() - t0) * 1000.0
        latencies_ms.append(latency_ms)

        print(
            f"Consumed event {event['event_id'][:8]} -> Predicted Duration: {prediction_payload['predicted_duration_minutes']} mins (latency: {latency_ms:.3f} ms)"
        )

    avg_lat = sum(latencies_ms) / len(latencies_ms)
    print(f"\nAverage event scoring latency: {avg_lat:.3f} ms")


if __name__ == "__main__":
    from producer import generate_ride_event

    sample_stream = [generate_ride_event() for _ in range(5)]
    simulate_event_consumer(sample_stream)
