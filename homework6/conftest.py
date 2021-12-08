import pytest

from task2 import Student, Teacher


@pytest.fixture(scope="session")
def teacher():
    return Teacher('Din', 'Vinchester')


@pytest.fixture(scope="session")
def student():
    return Student('Tom', 'Hiddlston')
