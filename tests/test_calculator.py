import pytest
from app.calculator import add  # import the function you want to test

# Parametrized test (runs multiple cases)
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 20, 30)
])
def test_add(a, b, result):
    assert add(a, b) == result