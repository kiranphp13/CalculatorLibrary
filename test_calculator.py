"""
Unit tests for the calculator library
"""
from calculator import (add, subtract)

def test_add():
    result = add(4, 4)
    assert result == 8

def test_subtract():
    result = subtract(4, 4)
    assert result == 0

