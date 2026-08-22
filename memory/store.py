from __future__ import annotations

from typing import Any


class MemoryStore:
    """Minimal in-memory store for workflow artifacts."""

    def __init__(self) -> None:
        self.items: list[dict[str, Any]] = []

    def add(self, item: dict[str, Any]) -> None:
        self.items.append(dict(item))
