def review(items: list[str]) -> dict[str, object]:
    """Record supplied environment-review items for qualified human review."""
    return {"items": list(items), "reviewed": True}
