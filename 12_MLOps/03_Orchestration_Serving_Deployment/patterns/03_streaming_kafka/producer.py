"""Inference Pattern 3: Streaming Event Producer (producer.py).

Simulates incoming ride booking events pushed onto an event bus (Kafka / RabbitMQ / Redis Streams).
"""

import json
import time
import uuid
import numpy as np


def generate_ride_event() -> dict:
    """Generates a realistic single ride request event."""
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": time.time(),
        "ride_info": {
            "PULocationID": int(np.random.randint(1, 265)),
            "DOLocationID": int(np.random.randint(1, 265)),
            "trip_distance": float(round(np.random.exponential(3.2) + 0.2, 2)),
            "passenger_count": int(np.random.choice([1, 2, 3])),
            "hour_of_day": int(time.localtime().tm_hour),
            "day_of_week": int(time.localtime().tm_wday),
        },
    }


def produce_events_stream(n_events: int = 10, delay_seconds: float = 0.1):
    """Produces a continuous stream of events."""
    print(f"Emitting {n_events} ride booking events...")
    for i in range(1, n_events + 1):
        event = generate_ride_event()
        event_json = json.dumps(event)
        print(f"[{i}/{n_events}] Produced Event -> ID: {event['event_id'][:8]} | Distance: {event['ride_info']['trip_distance']} mi")
        time.sleep(delay_seconds)


if __name__ == "__main__":
    produce_events_stream(n_events=5, delay_seconds=0.2)
