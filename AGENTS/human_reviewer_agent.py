from __future__ import annotations

from typing import Any


class HumanReviewerAgent:
    """Expose explicit qualified-human approval without granting treatment authority."""

    name = "human_reviewer"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "approved": context.get("human_approval") is True,
            "treatment_authority": False,
            "human_review_required": True,
        }
