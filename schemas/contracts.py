from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RehabilitationContext:
    """Typed container for non-prescriptive rehabilitation workflow inputs."""

    goals: list[dict[str, Any]] = field(default_factory=list)
    sessions: list[dict[str, Any]] = field(default_factory=list)
    progress: dict[str, Any] = field(default_factory=dict)
