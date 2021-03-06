import pytest

from homework4.task_4 import fizzbuzz


def test_fizzbuzz_return_correct_answer():
    """Testing correct working"""
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']


def test_fizzbuzz_negative_integer():
    """Testing working with negative integer"""
    assert fizzbuzz(-1) == []


def test_fizzbuzz_not_integer_element():
    """Testing working with not integer element"""
    with pytest.raises(ValueError):
        fizzbuzz(2.3)
