from task5 import find_maximal_subarray_sum


def test_find_maximal_sum():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_error():
    with pytest.raises(ValueError):
        find_maximal_subarray_sum([], 2)
