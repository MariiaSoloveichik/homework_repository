from pathlib import Path

from homework9.task3 import universal_file_counter


def test_token_case(tmpdir):
    """Test count with token"""
    tmpdir.join("1.txt").write("0 1\n2 3\n4 5\n6 7\n8 9\n")
    tmpdir.join("2.txt").write("a b c\nd e f\n")
    tmpdir.join("3.txt").write("123 124 125\n")
    assert (universal_file_counter(Path(str(tmpdir)), "txt", str.split)) == 8


def test_no_token_case(tmpdir):
    """Test count without token"""
    tmpdir.join("1.txt").write("0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n")
    tmpdir.join("2.txt").write("a\nb\nc\nd\ne\nf\n")
    tmpdir.join("3.txt").write("123\n124\n125\n")
    assert universal_file_counter(Path(str(tmpdir)), "txt") == 19
