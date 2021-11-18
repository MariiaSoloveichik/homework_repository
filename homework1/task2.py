"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from math import sqrt
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Check if a sequence of integers is a Fibonacci sequence
    param data - Sequence to check
    return - Is a Fib sequence
    """
    def is_square(n: int):
        """Returns if the given number is a perfect square."""
        return n == int(sqrt(n)) ** 2

    def is_valid(n: int):
        """Returns if the given number is a Fibonacci number."""
        return is_square(5 * n ** 2 + 4) or is_square(5 * n ** 2 - 4)

    if len(data) == 0 or len(data) == 1:
        return False

    if not is_valid(data[0]) or not is_valid(data[1]):
        return False

    for i in range(2, len(data)):
        if not (data[i] == data[i - 1] + data[i - 2]):
            return False
        data = data[1:]
    return True
