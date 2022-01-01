"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


@contextmanager
def supressor(exception):
    """
    Сontext manager, that suppresses passed exception.
    :param exception:  any exception
    """
    try:
        yield
    except exception:
        pass


class Supressor:
    """
    Сontext manager, that suppresses passed exception.
    """
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exception is exc_type
