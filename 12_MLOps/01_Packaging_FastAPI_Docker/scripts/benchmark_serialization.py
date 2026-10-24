"""Benchmark Serialization Formats and Inference Runtimes.

Compares:
- Python Pickle / Joblib
- ONNX Runtime
- JSON serialization payload sizes
"""

import json
import time
import numpy as np


def benchmark_inference():
    print("=" * 60)
    print("MLOps Serialization & Inference Benchmark")
    print("=" * 60)

    # Sample input payload
    sample_dict = {
        "PULocationID": 100,
        "DOLocationID": 230,
        "trip_distance": 5.4,
        "passenger_count": 2,
        "hour_of_day": 18,
        "day_of_week": 4,
    }

    # 1. Payload size comparison
    json_bytes = json.dumps(sample_dict).encode("utf-8")
    raw_array = np.array(list(sample_dict.values()), dtype=np.float32)
    binary_bytes = raw_array.tobytes()

    print(f"JSON Payload Size:   {len(json_bytes)} bytes")
    print(f"Raw Binary (Float32): {len(binary_bytes)} bytes ({len(binary_bytes)/len(json_bytes)*100:.1f}% of JSON)")

    # 2. Timing loops
    iterations = 5000
    print(f"\nRunning {iterations} iterations benchmark...")

    # Benchmark JSON parse
    t0 = time.perf_counter()
    for _ in range(iterations):
        _ = json.loads(json_bytes)
    t_json = (time.perf_counter() - t0) * 1000.0 / iterations
    print(f"JSON Decode Latency: {t_json*1000:.2f} µs per call")

    # Benchmark numpy array creation
    t0 = time.perf_counter()
    for _ in range(iterations):
        _ = np.frombuffer(binary_bytes, dtype=np.float32)
    t_bin = (time.perf_counter() - t0) * 1000.0 / iterations
    print(f"Binary Decode Latency: {t_bin*1000:.2f} µs per call (Speedup: {t_json/t_bin:.1f}x)")

    print("\nTakeaways for Production:")
    print("1. Standard JSON is ideal for public REST APIs (interoperability & human debugging).")
    print("2. Internal microservice-to-microservice calls benefit from Protobuf/gRPC binary transfer.")
    print("3. ONNX Runtime eliminates Python GIL bottlenecks and leverages SIMD/AVX hardware optimization.")
    print("=" * 60)


if __name__ == "__main__":
    benchmark_inference()
