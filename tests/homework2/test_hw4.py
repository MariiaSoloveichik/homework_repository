from homework_rep.homework2.hw2_task_4.py import cache_func


def test_cache_func():
    """ Accepts another function as an argument and return
    such a function, every call to initial one cached."""
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2
