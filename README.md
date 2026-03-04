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

# Parameterize Test Basic Syntax:
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
