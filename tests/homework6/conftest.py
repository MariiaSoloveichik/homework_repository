from homework6.task2 import Student, Teacher

import pytest


@pytest.fixture(scope="session")
def teacher():
    return Teacher('Din', 'Vinchester')


@pytest.fixture(scope="session")
def student():
    return Student('Tom', 'Hiddlston')
