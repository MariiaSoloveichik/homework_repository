import pytest

from homework6.task2 import DeadlineError, Student, Teacher


def test_Student_attributes():
    """Testing student attributes"""
    lazy_student = Student('Roman', 'Petrov')
    assert lazy_student.first_name == 'Roman' and \
        lazy_student.last_name == 'Petrov'


def test_Teacher_attributes():
    """Testing teacher attributes"""
    opp_teacher = Teacher('Daniil', 'Shadrin')
    assert opp_teacher.first_name == 'Daniil' and \
        opp_teacher.last_name == 'Shadrin'


def test_deadline_exception_function(teacher, student):
    """Testing DeadlineError"""
    oop_hw = teacher.create_homework('Learn OOP', 0)
    with pytest.raises(DeadlineError):
        student.do_homework(oop_hw, "I've done this homework")
