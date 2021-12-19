from homework7.task2 import backspace_compare


def test_positive_lowercase():
    """Testing equal lowercase strings"""
    assert backspace_compare("ab#c", "ad#c") is True


def test_hashtag():
    """Testing equal lowercase strings"""
    assert backspace_compare("a##c", "#a#c") is True


def test_negative_case():
    """Testing equal lowercase strings"""
    assert backspace_compare("a#c", "b") is False


def test_positive_upper():
    """Testing equal lowercase strings"""
    assert backspace_compare("#A#C", "A##C") is True
