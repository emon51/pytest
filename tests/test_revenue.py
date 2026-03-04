import pytest

from app.revenue import max_revenue


def test_max_revenue(revenue_cases):
    for days, expected in revenue_cases:
        assert max_revenue(days) == expected


def test_max_revenue_raises_on_empty_input():
    with pytest.raises(ValueError, match="days must not be empty"):
        max_revenue([])
