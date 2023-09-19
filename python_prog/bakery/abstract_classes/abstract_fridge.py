from abstract_classes.abstract_fruit import Fruit
from abstract_classes.abstract_storage import Storage
from errors.storage_errors import FridgeForFruits


class Fridge(Storage):
    def __setitem__(self, key, value):
        if not Fruit in value.__class__.mro():
            raise FridgeForFruits()
        self.storage[key] = value