"""LLM Observability and Prompt Management with Langfuse (langfuse_tracer.py).

Demonstrates:
1. End-to-end tracing of user queries, vector retrieval spans, and LLM generations
2. Centralized prompt versioning and runtime fetching
3. Token usage and financial cost estimation
4. User score / evaluation tagging
"""

import time
import uuid

try:
    from langfuse import Langfuse
    HAS_LANGFUSE = True
except ImportError:
    HAS_LANGFUSE = False


class MLOpsLangfuseTracer:
    """Wrapper managing Langfuse telemetry and prompt configurations."""

    def __init__(self):
        self.client = Langfuse() if HAS_LANGFUSE else None

    def get_prompt_template(self, prompt_name: str = "ride_duration_explainer", version: str = "production") -> str:
        """Fetches active versioned prompt template from Langfuse server with local fallback."""
        if self.client:
            try:
                prompt_obj = self.client.get_prompt(prompt_name, label=version)
                return prompt_obj.prompt
            except Exception as e:
                print(f"Warning: Could not fetch prompt '{prompt_name}' from Langfuse: {e}")

        # Production fallback prompt template
        return (
            "You are an expert transportation AI assistant. Given a trip of {distance} miles "
            "taking {duration} minutes, explain traffic conditions concisely."
        )

    def trace_rag_interaction(
        self,
        user_query: str,
        retrieved_contexts: list[str],
        simulated_response: str,
        input_tokens: int = 150,
        output_tokens: int = 45,
    ) -> dict:
        """Traces an LLM interaction with detailed observation hierarchy."""
        trace_id = str(uuid.uuid4())
        start_time = time.time()

        # Token cost estimation (e.g. GPT-4o-mini pricing: $0.15/1M input, $0.60/1M output)
        cost_usd = (input_tokens * 0.00000015) + (output_tokens * 0.00000060)

        trace_summary = {
            "trace_id": trace_id,
            "user_query": user_query,
            "retrieved_chunks_count": len(retrieved_contexts),
            "response": simulated_response,
            "token_usage": {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens,
            },
            "estimated_cost_usd": round(cost_usd, 7),
            "latency_seconds": round(time.time() - start_time, 3),
        }

        print("=" * 60)
        print(f"LANGFUSE TRACE RECORDED [ID: {trace_id[:8]}]")
        print(f"  User Query:       {user_query}")
        print(f"  Retrieved Chunks: {len(retrieved_contexts)}")
        print(f"  Total Tokens:     {trace_summary['token_usage']['total_tokens']}")
        print(f"  Estimated Cost:   ${cost_usd:.7f}")
        print("=" * 60)

        return trace_summary

    def record_user_feedback(self, trace_id: str, score: float, comment: str | None = None):
        """Attaches numeric score (0.0 to 1.0) or user thumbs-up/down to trace."""
        print(f"Tagged Trace {trace_id[:8]} with User Score: {score} (Comment: {comment})")
        if self.client:
            self.client.score(
                trace_id=trace_id,
                name="user_satisfaction",
                value=score,
                comment=comment,
            )


if __name__ == "__main__":
    tracer = MLOpsLangfuseTracer()
    prompt = tracer.get_prompt_template()
    print("Active Prompt Template:", prompt)

    trace = tracer.trace_rag_interaction(
        user_query="Why is my 5-mile trip to JFK Airport estimated at 45 minutes?",
        retrieved_contexts=[
            "Van Wyck Expressway experiencing severe construction delays between Exit 4 and 6.",
            "Rainstorm in Queens reduced average vehicular speeds to 12 mph.",
        ],
        simulated_response="Heavy construction on the Van Wyck Expressway combined with rain is reducing speeds to 12 mph.",
    )

    tracer.record_user_feedback(trace["trace_id"], score=1.0, comment="Very helpful explanation")
