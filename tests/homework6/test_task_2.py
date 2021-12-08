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


def test_homework_done_class_attribute(teacher, student):
    """Testing that homework_done is
    the same thing for class and instance of class"""
    oop_hw = teacher.create_homework('Learn OOP', 1)
    result_1 = student.do_homework(oop_hw, "I've done this homework")
    teacher.check_homework(result_1)
    temp_1 = teacher.homework_done

    teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_deadline_exception_function(teacher, student):
    """Testing DeadlineError"""
    oop_hw = teacher.create_homework('Learn OOP', 0)
    with pytest.raises(DeadlineError):
        student.do_homework(oop_hw, "I've done this homework")
