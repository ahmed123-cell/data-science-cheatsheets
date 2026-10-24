"""vLLM Streaming Client with Time-To-First-Token (TTFT) Measurement (stream_client.py).

Demonstrates Server-Sent Events (SSE) streaming and measuring key LLM metrics:
- TTFT (Time to First Token)
- ITL (Inter-Token Latency)
- Total Generation Throughput (tokens/second)
"""

import time


def simulate_streaming_generation(prompt: str = "Explain MLOps maturity levels in 3 bullet points."):
    """Simulates real-time token streaming from an LLM server."""
    print(f"User Prompt: '{prompt}'")
    print("Initiating streaming request...")

    simulated_tokens = [
        "MLOps ", "Maturity ", "Levels:\n",
        "1. ", "Level ", "0: ", "Manual ", "notebooks, ", "no ", "tracking.\n",
        "2. ", "Level ", "2: ", "Automated ", "training ", "pipelines ", "(DVC, ", "Airflow).\n",
        "3. ", "Level ", "4: ", "Full ", "autonomous ", "CI/CD ", "with ", "drift-triggered ", "retraining.",
    ]

    request_start = time.perf_counter()
    first_token_time = None
    token_times = []

    print("\n[Streaming Output]")
    for i, token in enumerate(simulated_tokens):
        # Simulate network & inference delay
        if i == 0:
            time.sleep(0.08)  # TTFT delay
            first_token_time = time.perf_counter()
        else:
            time.sleep(0.02)  # Inter-token delay

        token_times.append(time.perf_counter())
        print(token, end="", flush=True)

    total_time = time.perf_counter() - request_start
    ttft_ms = (first_token_time - request_start) * 1000.0
    throughput = len(simulated_tokens) / total_time

    print("\n\n" + "=" * 50)
    print("STREAMING PERFORMANCE METRICS")
    print(f"  Total Tokens:         {len(simulated_tokens)}")
    print(f"  Time to First Token:  {ttft_ms:.1f} ms  (Target: < 200 ms)")
    print(f"  Total Duration:       {total_time:.2f} s")
    print(f"  Throughput:           {throughput:.1f} tokens/sec")
    print("=" * 50)


if __name__ == "__main__":
    simulate_streaming_generation()
