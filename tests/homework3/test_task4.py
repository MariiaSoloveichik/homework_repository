from homework3.task4 import is_armstrong


def test_is_armstrong_positive():
    """ Testing truly Armstrong numbers  """
    assert is_armstrong(153) is True


def test_is_armstrong_negative():
    """ Testing not Armstrong numbers  """
    assert is_armstrong(165) is False


def test_is_armstrong():
    """ Testing negative numbers  """
    assert is_armstrong(370) is True
