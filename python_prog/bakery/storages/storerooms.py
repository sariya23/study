from abstract_classes.abstract_fridge import Fridge
from abstract_classes.abstract_storeroom import Storeroom
from bake import BlackBread
from fruits import Banana


class SmallStoreroom(Storeroom):
    def __init__(self):
        super().__init__(5)


class MediumStoreroom(Storeroom):
    def __init__(self):
        super().__init__(10)


class BigStoreroom(Storeroom):
    def __init__(self):
        super().__init__(15)


if __name__ == '__main__':
    s = SmallStoreroom()

    s[0] = BlackBread(1, -100, 1)