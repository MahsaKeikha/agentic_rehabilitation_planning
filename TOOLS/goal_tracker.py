from __future__ import annotations

from typing import Any


def track(goals: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a deterministic summary of supplied rehabilitation goals."""
    return {"goals": list(goals), "count": len(goals)}
