from typing import Callable

storage = dict()


def cache(times: int) -> Callable:
    assert times >= 0

    def decorator(func: Callable) -> Callable:
        def wrapper(*args):
            key = (func.__name__, args)
            if key in storage:
                res, remaining_times = storage[key]
                if remaining_times > 0:
                    storage[key] = (res, remaining_times - 1)
                    return res
            res = func(*args)
            storage[key] = (res, times - 1)
            return res

        return wrapper

    return decorator
