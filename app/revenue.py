def max_revenue(days: list[int]) -> int:
    result: int = days[0]
    curr: int = days[0]

    for revenue in days[1:]:
        curr = max(revenue, curr + revenue)
        result = max(result, curr)

    return result