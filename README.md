# Basic Structure: 
```bash
project/
│
├── app/
│   ├── calculator.py
│   └── revenue.py
│
├── tests/
│   ├── test_calculator.py
│   └── test_revenue.py
│
├── requirements.txt
├── pytest.ini
└── venv/
```

# Parametrized Test:
### Syntax:
1. import pytest
2. import the function to test
3. @pytest.mark.parametrize("param1,param2", [ (val1,val2), ... ])
4. define a test function with same parameter names
5. assert that function output matches expected result

## Example
```bash
import pytest
from app.calculator import add  # import the function we want to test

# Parametrized test (runs multiple test cases)
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 20, 30)
])
def test_add(a, b, result):
    assert add(a, b) == result
```

# pytest.ini 
```bash

# This tells pytest: "The following configuration belongs to pytest."
# Without it, pytest ignores the file.
[pytest]

# Directory where pytest will look for tests
# Instead of scanning the whole project, it will only search inside "tests/"
testpaths = tests

# Pattern for test file names
# pytest will only collect files that match this pattern
# Example: test_math.py, test_api.py
python_files = test_*.py

# -v means verbose mode (shows detailed test results)
addopts = -v
```

# Fixtures: 
Fixtures is “ready-to-use test resources” for tests — setup done once, reused everywhere.
### Syntax: 
1. Define fixture: @pytest.fixture
2. Return or yield resources
3. Use fixture: pass its name as a test function parameter
4. Pytest injects the value automatically



# Pytest Core Concepts: 
- Fixtures for reusable setup/data
- Parameterized tests for multiple test cases
- Exception testing with pytest.raises()

# Practice Problems: 
## 1. Testing a Function with Multiple Inputs (Parametrize)
Code:
```bash
def multiply(a: int, b: int) -> int:
    return a * b
```
### Practice Task: 
Write a pytest test using parametrize for:
```bash
(2,3) → 6
(4,5) → 20
(10,0) → 0
```
### Goal: practice @pytest.mark.parametrize
Solution:
```bash
import pytest 
def multiply(a: int, b: int) -> int:
    return a * b

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (4, 5, 20), 
    (10, 0, 0)
])
def test_multiply(a: int, b: int, expected: int) -> None:
    assert multiply(a, b) == expected
```

## 2. Testing Exceptions
Code:
```bash
def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
```
### Practice Task: 
Write a test for:
```bash
1. withdraw(100, 50) → 50
2. withdraw(100, 150) → should raise ValueError
```
### Goal: practice pytest.raises()
Solution:
```bash
import pytest 

def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount


def test_withdraw_success():
    assert withdraw(100, 50) == 50


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(100, 150)
```
## 3. Using Fixtures for Reusable Data
Code:
```bash
def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)
```
### Practice Task: 
Create a fixture that returns:
```bash
[10, 20, 30, 40]
```
Then write a test verifying the average is **25**.
### Goal: practice fixtures
Solution:
```bash
import pytest 
def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

@pytest.fixture
def numbers() -> list[int]:
    return [10, 20, 30, 40]

def test_average(numbers: list[int]) -> None:
    assert average(numbers) == 25
# It's optional for the problem but a professional test should also check empty list
def test_average_emty():
    with pytest.raises(ZeroDivisionError):
        average([])
# sum([]) / len([])
#  0 / 0
# ZeroDivisionError
```

## 4. Testing Edge Cases
Code:
```bash
def is_even(n: int) -> bool:
    return n % 2 == 0
```
### Practice Task: 
Create a test for:
```bash
2 → True
3 → False
0 → True
-2 → True
```
### Goal: practice edge cases
Solution:
```bash
import pytest 

def is_even(n: int) -> bool:
    if n < 0:
        raise ValueError("number can't be negative")
    return n % 2 == 0

@pytest.mark.parametrize("n, expected", [
    (0, True), 
    (2, True), 
    (3, False)
])
def test_is_even(n: int, expected: bool) -> None:
    assert is_even(n) == expected 

def test_is_even_negative() -> None:
    with pytest.raises(ValueError):
        is_even(-2)
```

## 5. Fixture + Parametrize Together (Professional Pattern)
Code:
```bash
def power(base: int, exp: int) -> int:
    return base ** exp
```
### Practice Task: 
Create a fixture containing:
```bash
(2,2,4)
(3,2,9)
(5,3,125)
```
Then write a test that loops through them.
### Goal: combine fixtures + assertions
Solution:
```bash
import pytest 
def power(base: int, exp: int) -> int:
    return base ** exp

@pytest.fixture 
def test_cases() -> list[tuple[int, int, int]]:
    return [
        (2, 2, 4), 
        (3, 2, 9), 
        (5, 3, 125)
    ]

def test_power(test_cases: list[tuple[int, int, int]]) -> None:
    for base, exp, expected in test_cases:
        assert power(base, exp) == expected 
        
```




































