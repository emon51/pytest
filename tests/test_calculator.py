import pytest
from app.calculator import add, divide


def test_add(add_cases):
    for a, b, expected in add_cases:
        assert add(a, b) == expected


def test_divide(divide_cases):
    for a, b, expected in divide_cases:
        assert divide(a, b) == expected


def test_divide_by_zero(divide_by_zero_case):
    a, b = divide_by_zero_case
    with pytest.raises(ZeroDivisionError):
        divide(a, b)
