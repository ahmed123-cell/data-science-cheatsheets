"""Release Strategy 2: Deterministic A/B Testing Router (ab_testing_router.py).

Splits user traffic deterministically using a hash of the user ID (e.g. 50/50 split),
ensuring that the same user consistently receives the same model experience.
"""

import hashlib


class ABTestRouter:
    """Routes requests between Model A (Control) and Model B (Challenger)."""

    def __init__(self, split_ratio: float = 0.50):
        self.split_ratio = split_ratio  # 0.50 = 50% traffic to Model B

    def route_user(self, user_id: str) -> str:
        """Deterministically hashes user_id to bucket [0.0, 1.0)."""
        # MD5 hash modulo 10000 gives 4 decimals of precision
        hash_val = int(hashlib.md5(user_id.encode("utf-8")).hexdigest(), 16)
        normalized = (hash_val % 10000) / 10000.0

        if normalized < self.split_ratio:
            return "model_b_challenger"
        else:
            return "model_a_control"


if __name__ == "__main__":
    router = ABTestRouter(split_ratio=0.5)
    sample_users = [f"user_{i:04d}" for i in range(10)]
    print("=" * 50)
    print("DETERMINISTIC A/B TESTING ROUTING")
    print("=" * 50)
    for u in sample_users:
        target = router.route_user(u)
        print(f"User: {u} -> Routed to: {target}")

    # Verify determinism: same user always hits same model
    assert router.route_user("user_0001") == router.route_user("user_0001")
    print("\nVerified: User routing is 100% deterministic and stateless.")
