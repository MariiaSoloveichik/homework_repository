from homework4.task_4 import fizzbuzz
import pytest

def test_fizzbuzz_return_correct_answer():
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']


def test_fizzbuzz_negative_integer():
    assert fizzbuzz(-1) == []


def test_fizzbuzz_not_integer_element():
    with pytest.raises(ValueError):
        fizzbuzz(2.3)
