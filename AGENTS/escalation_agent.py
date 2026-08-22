from __future__ import annotations

from typing import Any


class EscalationAgent:
    """Route supplied safety flags to qualified human review."""

    name = "escalation"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        flags = list(context.get("flags", []))
        return {
            "flags": flags,
            "escalate": bool(flags),
            "destination": "qualified_human" if flags else "routine_review",
        }
