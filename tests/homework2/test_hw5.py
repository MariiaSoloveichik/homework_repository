import string

from homework_rep.homework2.hw2_task_5.py import custom_range


def test_1_custom_range():
    """Accepts any iterable of unique values and then it behaves
    as range function."""
    assert = custom_range(string.ascii_lowercase, 'g') == \
             ['a', 'b', 'c', 'd', 'e', 'f']


def test_1_custom_range():
    assert = custom_range(string.ascii_lowercase, 'g', 'p') == \
             ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_1_custom_range():
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==\
             ['p', 'n', 'l', 'j', 'h']