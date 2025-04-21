import pytest
from services.calculator_service import add_numbers

def test_empty_string_returns_zero():
    result, negatives = add_numbers("")
    assert result == 0
    assert negatives == []

def test_single_number():
    result, negatives = add_numbers("5")
    assert result == 5
    assert negatives == []

def test_two_numbers():
    result, negatives = add_numbers("1,2")
    assert result == 3
    assert negatives == []

def test_multiple_numbers():
    result, negatives = add_numbers("1,2,3,4")
    assert result == 10
    assert negatives == []

def test_newline_as_delimiter():
    result, negatives = add_numbers("1\n2,3")
    assert result == 6
    assert negatives == []

def test_custom_delimiter():
    result, negatives = add_numbers("//;\n1;2")
    assert result == 3
    assert negatives == []

def test_negative_numbers_raise():
    result, negatives = add_numbers("1,-2,3,-4")
    assert result == 0
    assert negatives == [-2, -4]
