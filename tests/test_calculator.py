import pytest
from app.calculator import add, divide  # import the function you want to test

# Parametrized test (runs multiple cases)
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 20, 30)
])
def test_add(a, b, result):
    assert add(a, b) == result


@pytest.mark.parametrize("a, b, result", [
    ( 10, 2, 5),
    (20, 4, 5),
    (15, 3, 5)
])
def test_divide(a, b, result):
    assert divide(a, b) == result

# Test for division by zero
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
       