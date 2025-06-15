import pytest
from assertpy import assert_that
import json

test_data = [
    (3, 5, 15),
    (4, 5, 20),
    (5, 5, 25),
    (2, 10, 20),
    (10, 10, 100),
    (0, 5, 0),
    (-1, 5, -5),
    (-2, -5, 10),
    (100, 1, 100),
    (7, 3, 21)
]


@pytest.mark.parametrize("x, y, result", test_data)
def test_result_of_multiplication(x, y, result):
    assert x * y == result
    assert_that(x * y).is_equal_to(result)


def load_test_data_from_json():
    with open('tests/test_data.json', 'r') as f:
        data = json.load(f)
    return [(item['x'], item['y'], item['result']) for item in data]


@pytest.mark.parametrize("x, y, result", load_test_data_from_json())
def test_result_of_multiplication_with_external_json(x, y, result):
    assert x * y == result
    assert_that(x * y).is_equal_to(result)

# def test_result_of_multiplication():
#     x = 3
#     y = 5
#     assert x * y == 15


# def test_result_of_multiplication_2():
#     x = 4
#     y = 5
#     assert x * y == 20


# def test_result_of_multiplication_3():
#     x = 5
#     y = 5
#     assert x * y == 25