from __future__ import annotations

from typing import Any


def apply(progress: dict[str, Any]) -> dict[str, Any]:
    """Track supplied rehabilitation progress without inventing measurements."""
    return {"progress": dict(progress), "tracked": True, "inferred": False}
