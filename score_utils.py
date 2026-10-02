def average(scores):
    """Return the arithmetic mean of scores."""
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores) / len(scores)
