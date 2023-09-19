from abstract_classes.abstract_bake import Bake
from abstract_classes.abstract_storage import Storage
from errors.storage_errors import StoreroomForBake


class Storeroom(Storage):
    def __setitem__(self, key, value):
        if not Bake in value.__class__.mro():
            raise StoreroomForBake()
        self.storage[key] = value