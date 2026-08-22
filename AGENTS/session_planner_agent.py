from __future__ import annotations

from typing import Any


class SessionPlannerAgent:
    """Structure authorized rehabilitation sessions for qualified human review."""

    name = "session_planner"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "sessions": list(context.get("sessions", [])),
            "planned": True,
            "therapist_review_required": True,
        }
