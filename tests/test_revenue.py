import pytest
from app.revenue import max_revenue


@pytest.mark.parametrize("days,result", [
    ([300, -100, 400, -50, 200], 750),
    ([1, -2, 3, 4], 7),
    ([-5, -1, -3], -1)
])
def test_max_revenue(days, result):
    assert max_revenue(days) == result