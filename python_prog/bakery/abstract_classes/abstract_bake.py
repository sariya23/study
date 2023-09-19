from abc import abstractmethod, ABC
from validators.validators_nutrition import CorrectNutrition


class Bake(ABC):
    """
    Абстрактный класс представляет выпечку.

    От этого класса наследуются все объекты-выпечки.
    """
    proteins = CorrectNutrition()
    fats = CorrectNutrition()
    carbohydrates = CorrectNutrition()

    def __init__(self, proteins: int, fats: int, carbohydrates: int):
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
