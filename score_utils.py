def average(scores):
    """Return the arithmetic mean of scores."""
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores) / len(scores)

def letter_grade(score):
    """Convert a score to a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"