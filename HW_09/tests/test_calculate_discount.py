import pytest
from HW_09.pages.calculate_discount import calculate_discount

test_data = [
        (3, 5, 8),
        (4, 5, 9),
        (5, 5, 10),
        (2, 10, 12),
        (10, 10, 20),
        (-2, -5, -7),

]
@pytest.mark.parametrize("discount_percent,expected",test_data)


def test_calculate_discount(base_price,discount_percent,expected):
 assert calculate_discount(base_price,discount_percent)==expected


