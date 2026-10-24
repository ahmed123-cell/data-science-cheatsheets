"""Release Strategy 1: Blue/Green Deployment Switcher (blue_green_deploy.py).

Maintains two identical production environments (Blue = Active, Green = Staging).
Switches routing instantly with zero downtime and instant rollback capability.
"""

import json
from pathlib import Path


class BlueGreenRouter:
    def __init__(self, config_path: Path = Path("router_state.json")):
        self.config_path = config_path
        self.state = self._load_state()

    def _load_state(self) -> dict:
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "active_color": "blue",
            "environments": {
                "blue": {"url": "http://127.0.0.1:8001", "version": "v1.0.0"},
                "green": {"url": "http://127.0.0.1:8002", "version": "v2.0.0"},
            },
        }

    def _save_state(self) -> None:
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2)

    def get_active_target(self) -> dict:
        active = self.state["active_color"]
        return self.state["environments"][active]

    def flip(self) -> str:
        current = self.state["active_color"]
        new_color = "green" if current == "blue" else "blue"
        self.state["active_color"] = new_color
        self._save_state()
        new_env = self.state["environments"][new_color]
        print(f"Switched active environment: {current.upper()} -> {new_color.upper()} (Target: {new_env['url']}, Version: {new_env['version']})")
        return new_color

    def rollback(self) -> str:
        print("ALERT: Health degradation detected. Initiating instant rollback!")
        return self.flip()


if __name__ == "__main__":
    router = BlueGreenRouter()
    print("Initial Active Target:", router.get_active_target())
    router.flip()
    print("New Active Target:", router.get_active_target())
    router.rollback()
