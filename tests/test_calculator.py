import pytest
from pages.calculator import add_func

test_data = [
        (3, 5, 8),
        (4, 5, 9),
        (5, 5, 10),
        (2, 10, 12),
        (10, 10, 20),
        (-2, -5, -7),

]

@pytest.mark.parametrize("x,y,expected",test_data)

def test_add(x,y,expected):
    assert add_func(x,y) == expected

