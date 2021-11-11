from task3 import find_maximum_and_minimum



def test__file_with_empty_strings_case():
    """Testing file with line-delimited integers and empty strings"""
    assert find_maximum_and_minimum("task3_test_file1.txt") == (1, 6)


def test__file_with_one_int_case():
    """Testing file with one integer"""
    assert find_maximum_and_minimum("task3_test_file2.txt") == (7, 7)
