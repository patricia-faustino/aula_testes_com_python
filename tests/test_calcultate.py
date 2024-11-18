import pytest

from src.calculate import sum, subtraction, multiply, division


def test_sum_positive():
    assert sum(2, 3) == 5
    assert sum(10, 5) == 15

def test_sum_negative():
    assert sum(2, 3) != 6
    assert sum(10, 5) != 14

def test_subtraction_positive():
    assert subtraction(10, 5) == 5
    assert subtraction(20, 10) == 10

def test_subtraction_negative():
    assert subtraction(10, 5) != 4
    assert subtraction(20, 10) != 9

def test_multiply_positive():
    assert multiply(3, 7) == 21
    assert multiply(10, 5) == 50

def test_multiply_negative():
    assert multiply(3, 7) != 20
    assert multiply(10, 5) != 49

def test_division_positive():
    assert division(10, 2) == 5
    assert division(20, 4) == 5

def test_division_negative():
    assert division(10, 2) != 6
    assert division(20, 4) != 6

def test_division_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        division(10, 0)