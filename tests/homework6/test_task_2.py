import pytest

from homework6.task2 import DeadlineError, Student, Teacher


def test_Student_attributes_2():
    """Testing student attributes"""
    lazy_student = Student('Roman', 'Petrov')
    assert lazy_student.first_name == 'Roman' and \
        lazy_student.last_name == 'Petrov'


def test_Teacher_attributes_2():
    """Testing teacher attributes"""
    opp_teacher = Teacher('Daniil', 'Shadrin')
    assert opp_teacher.first_name == 'Daniil' and \
        opp_teacher.last_name == 'Shadrin'
