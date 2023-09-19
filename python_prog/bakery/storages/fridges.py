from abstract_classes.abstract_fridge import Fridge


class SmallFridge(Fridge):
    """
    Маленький холодильник.
    """
    def __init__(self):
        super().__init__(5)


class MediumFridge(Fridge):
    """
    Средний холодильник.
    """
    def __init__(self):
        super().__init__(10)


class BigFridge(Fridge):
    """
    Большой холодильник.
    """
    def __init__(self):
        super().__init__(15)


