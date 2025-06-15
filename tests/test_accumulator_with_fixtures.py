import pytest
from pages.accumulator import Accumulator

@pytest.fixture(scope="function")
def accum_2():
    print("Setting up accum_2 fixture")
    return Accumulator()


def test_accum_creation(accum_2):
    assert accum_2.count == 0


def test_add_counts_twice(global_accum):
    global_accum.add_counts()
    global_accum.add_counts()
    assert global_accum.count == 2

def test_add_counts_with_params(accum_2):
    accum_2.count = 10
    assert accum_2.count == 10

def test_add_counts_with_global_10_accum(global_accum_with_10):
    assert global_accum_with_10.count == 10