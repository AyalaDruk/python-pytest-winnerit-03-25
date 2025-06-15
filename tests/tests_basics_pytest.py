from assertpy import assert_that

def test_numbers_sum():
    assert (2 + 2 == 5) == False


def test_numbers_sum_assertpy():
    assert_that(2 + 2 == 5).is_false()


def test_contains_substring():
    assert "abc" in "abcdefg"


def test_contains_substring_assertpy():
    assert_that("abcdefg").contains("abc")