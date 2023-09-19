from abstract_classes.abstract_fruit import Fruit
from abstract_classes.abstract_storage import Storage
from errors.storage_errors import FridgeForFruits


class Fridge(Storage):
    """
    Абстрактный класс, представляющий холодильник.

    Все размеры холодильника наследуются о него.
    """
    def __setitem__(self, key: int, value: Fruit):
        """
        В холодильнике могут лежать только объекты-фрукты.
        """
        if not Fruit in value.__class__.mro():
            raise FridgeForFruits()
        self.storage[key] = value