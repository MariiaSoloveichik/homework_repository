"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Homework:
    """Creates object of homework
    Attributes:
    text: Text of the task
    deadline: Number of days to complete
    created: Time and date of creation
    Methods:
    init: attributes
    is_active: Checks expired deadline
    """
    def __init__(self, text: str, deadline: int,
                 created: datetime.datetime) -> None:
        """
        attributes:
        text: Text of the task
        deadline: Number of days to complete
        created: Time and date of creation
        """
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = created

    def is_active(self) -> bool:
        """
        Checks expired deadline
        return boolean about expired deadline
        """
        if not datetime.datetime.now() < self.deadline + self.created:
            raise DeadlineError


class Teacher:
    """Creates teacher person
    Attributes
    last_name: Teacher's last name
    first_name: Teacher's first name
    Methods
    init: Set all required attributes
    create_homework: Static method. Creates and returns
    homework object
    """
    homework_done = defaultdict(list)

    def __init__(self, first_name: str, last_name: str) -> None:
        """
        attributes:
        last_name: Teacher's last name
        first_name: Teacher's first name
        """
        self.first_name = first_name
        self.last_name = last_name

    def check_homework(self, homework_res):
        """
        check_homework - accepts an instance of HomeworkResult and
        returns True
        if the student's response is more than 5 characters, also,
        if the check is successful, add to homework_done.
        """
        if len(homework_res.solution) >= 5:
            if homework_res not in self.homework_done[homework_res.homework]:
                self.homework_done[homework_res.homework].append(homework_res)
            return True
        return False

    @classmethod
    def reset_results(cls, homework_to_delete=None):
        """
        reset_results - if you pass the Homework instance,
        it deletes only the results of this task from
        homework_done, if you do not pass anything,
        it will completely reset homework_done.
        """
        if homework_to_delete is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework_to_delete)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
        Creates homework object
        text: Text of the task
        deadline: Number of days to complete
        return: Homework object
        """
        created = datetime.datetime.now()
        return Homework(text, deadline, created)


class Student(Teacher):
    def do_homework(self, homework: Homework, solution: str):
        """
        Static method for doing homework
        homework: Homework class object
        return Homework object or expired deadline warning
        """
        try:
            homework.is_active()
        except DeadlineError:
            raise DeadlineError("You are late")
        return HomeworkResult(self, homework, solution)


class HomeworkResult:
    """
        Result of student's homework.
    """
    def __init__(self, author: Student, homework:
                 Homework, solution: str) -> None:
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
