from __future__ import annotations

from typing import Any


def apply(environment: dict[str, Any]) -> dict[str, Any]:
    """Record an environment review without granting clinical clearance."""
    return {"environment": dict(environment), "reviewed": True, "clinical_clearance": False}
