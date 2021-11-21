from homework2.hw2_task_2 import major_and_minor_elem


def test_major_and_minor_elem():
    """ Find the most common and the least common elements"""
    assert major_and_minor_elem([1, 2, 3, 7, 6, 3, 45, 6,
                                 7, 9, 9, 9, 1, 2]) == (9, 45)
