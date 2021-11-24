import pytest

import homework4.task_1


def test_positive_case(temp_file):
    """Testing positive case"""
    temp_file.write_text("1\n223344\n556677\nprya\nnikc", encoding='utf-8')
    assert read_magic_number(temp_file)


def test_negative_case(temp_file):
    """Testing negative case"""
    temp_file.write_text("7\n223344\n556677\nprya\nnikc", encoding='utf-8')
    assert not read_magic_number(temp_file)


def test_value_error_case(temp_file):
    """Testing raise of ValueError"""
    temp_file.write_text("a b c\n223344\n556677\nprya\nnikc", encoding='utf-8')
    with pytest.raises(ValueError):
        read_magic_number(temp_file)


def test_no_file_case():
    """Testing raise of FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        read_magic_number("non-existing-file.txt")
