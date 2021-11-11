"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
import math
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    def is_fib_num(n: int) -> bool:
        """Check number is a Fibonacci number"""
        phi = 0.5 + 0.5 * math.sqrt(5.0)
        a = phi * n
        return n == 0 or abs(round(a) - a) < 1.0 / n

    if len(data) == 0 or len(data) == 1:
        return False

    elif len(data) == 2 and not (data[0] == 0 and data[1] == 1):
        return False

    for i in range(2, len(data)):
        if not (data[i] == data[i - 1] + data[i - 2]):
            return False
        data = data[1:]
    return True
