from homework1.task4 import check_sum_of_four


def test_regular_case():
    """Testing regular case"""
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 0], [0, 2]) == 4


def test_all_nums_are_zeros_case():
    """Testing of the wrong type"""
    assert check_sum_of_four([1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]) == 0


def test_empty_lists_case():
    """Testing empty case"""
    assert check_sum_of_four([], [], [], []) == 0
