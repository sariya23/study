from abstract_classes.abstract_fridge import Fridge


class SmallFridge(Fridge):
    def __init__(self):
        super().__init__(5)


class MediumFridge(Fridge):
    def __init__(self):
        super().__init__(10)


class BigFridge(Fridge):
    def __init__(self):
        super().__init__(15)


