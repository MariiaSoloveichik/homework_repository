from homework3.task2 import boost_slow_calculate


def test_regular_case():
    """Tests the boost_slow_calculate function.
    Comparing the result of the boost_slow_calculate function with the
    correct solution.
    :return: the truth of an expression
    :rtype: bool
    """
    assert boost_slow_calculate(range(500)) == 1024259



