from collections.abc import Sequence


def max_revenue(days: Sequence[int]) -> int:
    if not days:
        raise ValueError("days must not be empty")

    best = days[0]
    current = days[0]

    for value in days[1:]:
        current = max(value, current + value)
        best = max(best, current)

    return best
