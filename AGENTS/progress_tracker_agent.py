from __future__ import annotations

from typing import Any


class ProgressTrackerAgent:
    """Summarize supplied rehabilitation progress without inventing clinical facts."""

    name = "progress_tracker"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "progress": dict(context.get("progress", {})),
            "tracked": True,
            "inferred_clinical_facts": False,
        }
