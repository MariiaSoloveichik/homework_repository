import os

import pytest

from homework4.task_1 import read_magic_number


@pytest.fixture()
def create_and_del_true_file():
    with open(file='temp_file.txt', mode='w', encoding='utf8') as fi:
        fi.write("1\n223344\n556677\nprya\nnikc")
    yield
    os.remove('temp_file.txt')

@pytest.fixture()
def create_and_del_false_file():
    with open(file='temp_file.txt', mode='w', encoding='utf8') as fi:
        fi.write("7\n223344\n556677\nprya\nnikc")
    yield
    os.remove('temp_file.txt')


@pytest.fixture()
def create_and_del_exception_file():
    with open(file='temp_file.txt', mode='w', encoding='utf8') as fi:
        fi.write("a b c\n223344\n556677\nprya\nnikc")
    yield
    os.remove('temp_file.txt')


def test_positive_case(create_and_del_true_file):
    """Testing positive case"""
    assert read_magic_number('temp_file.txt') is True


def test_negative_case(create_and_del_false_file):
    """Testing negative case"""
    assert read_magic_number('temp_file.txt') is False


def test_value_error_case(create_and_del_exception_file):
    """Testing raise of ValueError"""
    with pytest.raises(ValueError):
        read_magic_number('temp_file.txt')


def test_no_file_case(create_and_del_false_file):
    """Testing raise of FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        read_magic_number("non-existing-file.txt")
