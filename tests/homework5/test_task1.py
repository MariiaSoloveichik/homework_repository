import datetime

from homework5.task_1 import Student, Teacher


def test_create_person():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    assert teacher.last_name == "Daniil" and student.first_name == "Petrov"


def test_create_homework():
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert (
        expired_homework.deadline == datetime.timedelta(0)
        and expired_homework.text == "Learn functions"
    )


def test_use_method():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")

    expired_homework = teacher.create_homework("Learn functions", 0)

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)

    assert (
        student.do_homework(oop_homework) == oop_homework
        and student.do_homework(expired_homework) != expired_homework
    )
