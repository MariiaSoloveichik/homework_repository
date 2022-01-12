from homework9.task1 import merge_sorted_files


def testing_two_files_case(tmpdir):
    """Testing merge two files"""
    temp_file1 = tmpdir.join("temp1.txt")
    temp_file2 = tmpdir.join("temp2.txt")
    temp_file1.write("0\n2\n3\n4\n5\n7\n8\n9\n")
    temp_file2.write("1\n6\n125\n")
    assert list(merge_sorted_files([temp_file1, temp_file2])) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 125
        ]


def testing_one_file_case(tmpdir):
    """Testing merge one file"""
    temp_file1 = tmpdir.join("temp1.txt")
    temp_file1.write("1\n3\n5\n")
    assert list(merge_sorted_files([temp_file1])) == [1, 3, 5]


def testing_no_files_case():
    """Testing merge zero files"""
    assert list(merge_sorted_files([])) == []
