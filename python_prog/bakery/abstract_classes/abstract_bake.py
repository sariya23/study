from abc import abstractmethod, ABC
from validators.validators_nutrition import CorrectNutrition


class Bake(ABC):
    """
    Абстрактный класс представляет выпечку.
    """
    proteins = CorrectNutrition()
    fats = CorrectNutrition()
    carbohydrates = CorrectNutrition()

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.nutrition_facts = [self.proteins, self.fats, self.carbohydrates]
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
