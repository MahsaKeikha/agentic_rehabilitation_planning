from __future__ import annotations

from typing import Any


def apply(goals: list[dict[str, Any]]) -> dict[str, Any]:
    """Organize supplied clinician-defined goals without prescribing treatment."""
    return {"goals": list(goals), "treatment_prescription": False}
