from __future__ import annotations

from typing import Any


class EquipmentEnvironmentAgent:
    """Review supplied equipment and environment information for human follow-up."""

    name = "equipment_environment"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "environment": dict(context.get("environment", {})),
            "reviewed": True,
            "clinical_clearance": False,
        }
