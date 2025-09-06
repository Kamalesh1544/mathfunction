import pytest
from main import add

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (1, 2, 3)  
])
def test_add(a, b, expected):
    assert add(a, b) == expected
