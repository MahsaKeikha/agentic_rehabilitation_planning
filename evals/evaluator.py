from __future__ import annotations

from typing import Any


REQUIRED_SPECIALISTS = (
    "goal_organizer",
    "session_planner",
    "progress_tracker",
    "equipment_environment",
    "escalation",
    "human_reviewer",
)


def evaluate(results: dict[str, Any]) -> dict[str, Any]:
    """Check that every required specialist produced an output."""
    missing = [name for name in REQUIRED_SPECIALISTS if name not in results]
    return {"passed": not missing, "missing": missing}
