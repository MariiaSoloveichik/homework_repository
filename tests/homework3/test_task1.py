import random

from homework3.task1 import cache


def random_function_with_args(*args):
    return random.randint(0, 100000), args


def test_cache_decorator():
    # create functions and arguments
    args = (1, "x", False)
    func = cache(times=5)(random_function_with_args)

    # run functions "times" times with same arguments
    result = func(args)
    for _ in range(4):
        # call with same arguments
        assert func(args) == result

        # extra call with different arguments should not make affect
        other_args = ("another_argument",)
        _, result_args = func(*other_args)
        assert result_args == other_args

    # cache should expire after function called "times" times with the same arguments
    assert func(args) != result
