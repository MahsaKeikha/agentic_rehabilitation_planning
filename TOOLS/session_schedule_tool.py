from __future__ import annotations

from typing import Any


def organize(items: list[dict[str, Any]]) -> dict[str, Any]:
    """Organize supplied session records without changing clinical content."""
    return {"sessions": list(items), "count": len(items)}
