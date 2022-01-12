from homework9.task2 import Supressor, supressor


def test_gen_suppressor():
    """Testing generator supressor func"""
    with supressor(IndexError):
        assert [][2]


def test_class_suppressor():
    """Testing generator supressor class"""
    with Supressor(IndexError):
        assert [][2]
