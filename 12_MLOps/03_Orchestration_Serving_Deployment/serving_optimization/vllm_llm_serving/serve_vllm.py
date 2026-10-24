"""Tier 5 Model Serving: vLLM High-Throughput LLM Engine (serve_vllm.py).

Explains how vLLM solves GPU memory fragmentation using PagedAttention
and continuous batching, serving open-weights LLMs (e.g. Qwen2.5, Llama-3).
"""

import subprocess
import sys


def print_vllm_architecture_guide():
    print("=" * 65)
    print("Tier 5 Serving: vLLM (Virtual Large Language Model Engine)")
    print("=" * 65)
    print("Key Innovations:")
    print("1. PagedAttention:")
    print("   - Traditional KV cache reserves contiguous GPU memory upfront (60-80% wasted).")
    print("   - PagedAttention allocates non-contiguous physical memory blocks like OS virtual memory.")
    print("   - Enables 2-4x higher batch sizes and throughput.")
    print("2. Continuous Batching (Iteration-Level Scheduling):")
    print("   - Traditional serving waits for all requests in a batch to finish generation.")
    print("   - Continuous batching evicts completed requests immediately and injects new ones per token iteration.")
    print("3. OpenAI-Compatible REST Server:")
    print("   - Drop-in replacement for OpenAI API endpoints (/v1/chat/completions, /v1/completions).")
    print("=" * 65)


def launch_vllm_command(model_name: str = "Qwen/Qwen2.5-7B-Instruct", port: int = 8000):
    """Prints the production command to launch vLLM OpenAI-compatible server."""
    cmd = [
        "python", "-m", "vllm.entrypoints.openai.api_server",
        "--model", model_name,
        "--port", str(port),
        "--max-model-len", "4096",
        "--gpu-memory-utilization", "0.90",
        "--trust-remote-code",
    ]
    print("\nTo launch vLLM on a GPU machine, execute:")
    print(" ".join(cmd))
    return cmd


if __name__ == "__main__":
    print_vllm_architecture_guide()
    launch_vllm_command()
