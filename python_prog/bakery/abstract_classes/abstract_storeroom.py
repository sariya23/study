from abstract_classes.abstract_bake import Bake
from abstract_classes.abstract_storage import Storage
from errors.storage_errors import StoreroomForBake


class Storeroom(Storage):
    """
    Абстрактный класс, представляющий склад.

    Склады всех размеров наследуются от него
    """
    def __setitem__(self, key: int, value: Bake):
        if not Bake in value.__class__.mro():
            raise StoreroomForBake()
        self.storage[key] = value