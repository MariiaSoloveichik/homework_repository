from homework1.task5 import find_maximal_subarray_sum


def test_find_maximal_sum():
    """Testing normal case"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_error():
    """Testing len(nums) == 0  case"""
    assert find_maximal_subarray_sum([], 2) == "Invalid input: empty list"


def test_short_list_case():
    """Testing 1 number list case"""
    assert find_maximal_subarray_sum([3], 1) == 3


def test_short_list_case_2():
    """Testing len(nums) < k"""
    assert find_maximal_subarray_sum([3, 2, -4], 6) == 5
