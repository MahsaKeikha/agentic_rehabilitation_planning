from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RunState:
    """Mutable workflow state containing only explicitly supplied artifacts."""

    phase: str = "goals"
    artifacts: dict[str, Any] = field(default_factory=dict)
