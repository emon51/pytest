import pytest


@pytest.fixture
def add_cases():
    return [
        (1, 2, 3),
        (2, 3, 5),
        (10, 20, 30),
    ]


@pytest.fixture
def divide_cases():
    return [
        (10, 2, 5),
        (20, 4, 5),
        (15, 3, 5),
    ]


@pytest.fixture
def divide_by_zero_case():
    return (10, 0)


@pytest.fixture
def revenue_cases():
    return [
        ([300, -100, 400, -50, 200], 750),
        ([1, -2, 3, 4], 7),
        ([-5, -1, -3], -1),
    ]
