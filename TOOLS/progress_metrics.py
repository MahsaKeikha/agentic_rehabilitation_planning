from __future__ import annotations

from typing import Any


def summarize(progress: dict[str, Any]) -> dict[str, Any]:
    """Summarize supplied progress data without inferring missing facts."""
    return {"progress": dict(progress), "measured": True, "inferred": False}
