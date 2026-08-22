from __future__ import annotations

from typing import Any


class TraceLog:
    """Collect lightweight workflow trace events."""

    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def record(self, stage: str, detail: Any) -> None:
        self.events.append({"stage": stage, "detail": detail})
