import pytest
from HW_09.pages.calculate_discount import calculate_discount

test_data = [
        (0, 100.0),
        (50, 50.0),
        (100, 0.0),
        (25.5, 74.5),
        (10, 90.0),
]
@pytest.mark.parametrize("discount_percent,expected",test_data)


def test_calculate_discount(base_price,discount_percent,expected):
 result= calculate_discount(base_price,discount_percent)
 assert result == expected


