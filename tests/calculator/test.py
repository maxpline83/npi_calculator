from src.calculator.npi_calculator import eval_npi
import unittest
import pytest

# test_eval_npi_pytest.py

def test_simple_addition():
    assert eval_npi("3 4 +") == 7

def test_complex_expression():
    assert eval_npi("3 4 + 16 *") == 60

def test_division():
    assert eval_npi("12 3 /") == 4

def test_negative_numbers():
    assert eval_npi("-5 3 +") == -2

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        eval_npi("5 0 /")
