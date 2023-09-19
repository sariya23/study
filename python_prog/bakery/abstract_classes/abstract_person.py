from abc import ABC, abstractmethod
from validators.validator_string import CorrectString


class Person(ABC):
    """
    Абстрактный класс, представляющий человека(в контексте сотрудника пекарни).
    """
    name = CorrectString()
    surname = CorrectString()
    post = CorrectString()

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass