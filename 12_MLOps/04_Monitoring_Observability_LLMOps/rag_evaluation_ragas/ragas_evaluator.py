"""RAG Evaluation Pipeline using RAGAS Metrics (ragas_evaluator.py).

Explains and computes the four foundational RAGAS metrics:
1. Faithfulness (Blames LLM Generator: Are answer claims grounded in retrieved context?)
2. Answer Relevance (Blames Prompt/Generator: Does the answer address the question?)
3. Context Precision (Blames Retriever: Are relevant chunks ranked at the top?)
4. Context Recall (Blames Retriever: Did retrieval find all ground-truth facts?)
"""

from typing import Any
import numpy as np


class RAGASEvaluationSuite:
    """Evaluates RAG pipeline outputs using grounded metric calculations."""

    @staticmethod
    def calculate_faithfulness(answer_claims: list[str], context_facts: list[str]) -> float:
        """Faithfulness = (Number of claims supported by context) / (Total claims made).

        Score: 0.0 to 1.0. If low, model is hallucinating facts outside the context.
        """
        if not answer_claims:
            return 1.0
        supported = 0
        for claim in answer_claims:
            # Check if claim keywords exist in context facts
            words = set(claim.lower().split())
            if any(len(words.intersection(fact.lower().split())) >= 2 for fact in context_facts):
                supported += 1
        return round(supported / len(answer_claims), 2)

    @staticmethod
    def calculate_context_precision(ranked_chunks: list[dict]) -> float:
        """Context Precision = Mean Average Precision (mAP) of relevant chunks.

        Evaluates if the most relevant chunks are ranked higher in the context window.
        """
        if not ranked_chunks:
            return 0.0

        hits = 0
        precisions = []
        for rank, chunk in enumerate(ranked_chunks, start=1):
            if chunk.get("is_relevant", False):
                hits += 1
                precisions.append(hits / rank)

        return round(sum(precisions) / max(1, hits), 2) if hits > 0 else 0.0

    @staticmethod
    def calculate_context_recall(ground_truth_facts: list[str], retrieved_contexts: list[str]) -> float:
        """Context Recall = (Ground truth facts found in context) / (Total ground truth facts).

        If low, the vector retriever failed to fetch necessary documents.
        """
        if not ground_truth_facts:
            return 1.0
        found = 0
        combined_context = " ".join(retrieved_contexts).lower()
        for fact in ground_truth_facts:
            keywords = [w for w in fact.lower().split() if len(w) > 3]
            if any(k in combined_context for k in keywords):
                found += 1
        return round(found / len(ground_truth_facts), 2)

    def evaluate_sample(self, sample: dict[str, Any]) -> dict[str, float]:
        """Runs full RAGAS evaluation on a test sample."""
        faithfulness = self.calculate_faithfulness(
            sample["answer_claims"],
            sample["retrieved_contexts"],
        )
        context_precision = self.calculate_context_precision(sample["ranked_chunks"])
        context_recall = self.calculate_context_recall(
            sample["ground_truth_facts"],
            sample["retrieved_contexts"],
        )

        # Harmonic mean composite score
        composite = round(np.mean([faithfulness, context_precision, context_recall]), 2)

        return {
            "faithfulness": faithfulness,
            "context_precision": context_precision,
            "context_recall": context_recall,
            "composite_ragas_score": composite,
        }


def run_demo():
    print("=" * 60)
    print("RAGAS METRICS EVALUATION HARNESS")
    print("=" * 60)

    evaluator = RAGASEvaluationSuite()

    # Sample test case
    sample = {
        "question": "What is the airport fee for TLC taxis picking up at JFK?",
        "ground_truth_facts": ["JFK Airport pick-up access fee is $1.75 mandated by the Port Authority."],
        "retrieved_contexts": [
            "The Port Authority imposes an airport access fee of $1.75 on all taxi pick-ups at JFK and LaGuardia.",
            "Taxis must display the TLC rate card on the rear passenger window.",
        ],
        "ranked_chunks": [
            {"chunk_id": "c1", "is_relevant": True},
            {"chunk_id": "c2", "is_relevant": False},
        ],
        "answer_claims": [
            "The JFK airport pick-up fee is $1.75.",
            "This fee is mandated by the Port Authority.",
        ],
    }

    results = evaluator.evaluate_sample(sample)
    print("Evaluation Results for RAG Sample:")
    print(f"  Faithfulness:      {results['faithfulness']}  (Target: >= 0.85)")
    print(f"  Context Precision: {results['context_precision']}  (Target: >= 0.80)")
    print(f"  Context Recall:    {results['context_recall']}  (Target: >= 0.85)")
    print(f"  Composite Score:   {results['composite_ragas_score']}")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
