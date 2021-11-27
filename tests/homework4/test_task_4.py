from homework4.task_4 import fizzbuzz


def test_fizzbuzz_return_correct_answer():
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']


def test_fizzbuzz_negative_integer():
    assert fizzbuzz(-1) == []


def test_fizzbuzz_not_integer_element():
    assert fizzbuzz(2.3) is ValueError("n have to be an integer")
