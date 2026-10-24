"""Release Strategy 3: Shadow Mode (Dark Launch) Proxy (shadow_mode_proxy.py).

Routes 100% of production traffic to the active model and returns the response immediately.
Asynchronously duplicates incoming traffic to the candidate shadow model, logging
predictions side-by-side to detect drift and compare latency before real rollout.
"""

import asyncio
import time
import uuid


async def mock_predict_production(features: dict) -> float:
    """Simulates production model inference."""
    await asyncio.sleep(0.015)  # 15 ms latency
    dist = features.get("trip_distance", 3.0)
    return round(5.0 + (dist * 2.5), 2)


async def mock_predict_shadow(features: dict) -> float:
    """Simulates candidate shadow model inference."""
    await asyncio.sleep(0.012)  # 12 ms latency
    dist = features.get("trip_distance", 3.0)
    # New neural network / candidate formula
    return round(4.8 + (dist * 2.45), 2)


async def shadow_worker(request_id: str, features: dict, prod_pred: float):
    """Background task logging shadow prediction alongside production prediction."""
    t0 = time.perf_counter()
    shadow_pred = await mock_predict_shadow(features)
    shadow_latency = (time.perf_counter() - t0) * 1000.0

    delta = abs(prod_pred - shadow_pred)
    print(
        f"[SHADOW LOG] Req: {request_id[:8]} | Prod: {prod_pred} mins | Shadow: {shadow_pred} mins | Delta: {delta:.2f} mins | Shadow Latency: {shadow_latency:.2f} ms"
    )


async def handle_shadow_request(features: dict) -> dict:
    """Handles client request in shadow mode."""
    request_id = str(uuid.uuid4())

    # 1. Primary synchronous path: Call production model
    prod_pred = await mock_predict_production(features)

    # 2. Asynchronous dark launch path: Fire and forget shadow prediction
    asyncio.create_task(shadow_worker(request_id, features, prod_pred))

    # 3. Immediately return production response to user (zero user impact!)
    return {
        "request_id": request_id,
        "predicted_duration": prod_pred,
        "served_by": "production_champion",
    }


async def main():
    print("=" * 60)
    print("SHADOW MODE (DARK LAUNCH) INFERENCE PROXY")
    print("=" * 60)
    sample_requests = [
        {"trip_distance": 2.5, "PULocationID": 10},
        {"trip_distance": 6.8, "PULocationID": 45},
        {"trip_distance": 14.2, "PULocationID": 120},
    ]

    for req in sample_requests:
        resp = await handle_shadow_request(req)
        print(f"Client Response -> Served: {resp['served_by']} | Output: {resp['predicted_duration']} mins")

    # Give background tasks time to complete output
    await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())
