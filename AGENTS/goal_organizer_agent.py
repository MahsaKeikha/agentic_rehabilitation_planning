from __future__ import annotations

from typing import Any


class GoalOrganizerAgent:
    """Organize clinician-defined rehabilitation goals without prescribing treatment."""

    name = "goal_organizer"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "goals": list(context.get("goals", [])),
            "organized": True,
            "treatment_prescription": False,
        }
