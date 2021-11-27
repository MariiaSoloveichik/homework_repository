"""
Write a function that takes a number N as
an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return list of n FizzBuzz numbers, n is integer """
    result = []
    if not isinstance(n, int):
        raise ValueError("n have to be an integer")
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("Fizz Buzz")
        elif num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(num))
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
