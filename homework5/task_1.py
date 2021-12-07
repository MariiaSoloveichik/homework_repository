"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


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
        if datetime.datetime.now() < self.created + self.deadline:
            return True
        return False


class Student:
    """Creates student person
    Attributes
    last_name: Student's last name
    first_name: Student's first name
    Methods
    init: attributes
    do_homework: Static method. Returns homework or
    expired deadline warning
    """
    def __init__(self, first_name: str, last_name: str) -> None:
        """
        attributes:
        last_name: Student's last name
        first_name: Student's first name
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Homework:
        """
        Static method for doing homework
        homework: Homework class object
        return Homework object or expired deadline warning
        """
        if homework.is_active():
            return homework
        print("You are late")
        return


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
    def __init__(self, first_name: str, last_name: str) -> None:
        """
        attributes:
        last_name: Teacher's last name
        first_name: Teacher's first name
        """
        self.first_name = first_name
        self.last_name = last_name

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
