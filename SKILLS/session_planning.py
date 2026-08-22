from __future__ import annotations

from typing import Any


def apply(sessions: list[dict[str, Any]]) -> dict[str, Any]:
    """Prepare supplied session data while preserving therapist authority."""
    return {"sessions": list(sessions), "therapist_review": True}
