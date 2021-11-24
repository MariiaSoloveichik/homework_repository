from homework2.hw2_task_3 import combinations


def test_1_combinations():
    """ Returns all possible lists with numbers"""
    assert combinations([1, 2, 3], [7], [6, 3]) == [
        [1, 7, 6],
        [1, 7, 3],
        [2, 7, 6],
        [2, 7, 3],
        [3, 7, 6],
        [3, 7, 3]]


def test_2_combinations():
    """ Returns all possible lists with letters"""
    assert combinations(['a', 's', 'f'], ['u'], ['k', 'o']) == [
        ['a', 'u', 'k'],
        ['a', 'u', 'o'],
        ['s', 'u', 'k'],
        ['s', 'u', 'o'],
        ['f', 'u', 'k'],
        ['f', 'u', 'o']]
