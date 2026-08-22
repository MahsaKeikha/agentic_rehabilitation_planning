def apply(flags: list[str]) -> dict[str, object]:
    """Route supplied safety flags toward qualified human escalation."""
    return {"flags": list(flags), "escalate": bool(flags)}
