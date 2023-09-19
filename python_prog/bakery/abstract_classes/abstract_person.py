from abc import ABC, abstractmethod

from validators.validator_string import CorrectString


class Person(ABC):
    name = CorrectString()
    surname = CorrectString()
    post = CorrectString()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass