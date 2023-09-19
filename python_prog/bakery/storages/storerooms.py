from abstract_classes.abstract_storeroom import Storeroom
from bake import BlackBread


class SmallStoreroom(Storeroom):
    """
    Маленький склад.
    """
    def __init__(self):
        super().__init__(5)


class MediumStoreroom(Storeroom):
    """
    Средний склад.
    """
    def __init__(self):
        super().__init__(10)


class BigStoreroom(Storeroom):
    """
    Большой слад.
    """
    def __init__(self):
        super().__init__(15)


if __name__ == '__main__':
    s = SmallStoreroom()

    s[0] = BlackBread(1, -100, 1)