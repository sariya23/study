from abstract_classes.abstract_bake import Bake


class WhiteBread(Bake):
    def __str__(self):
        return f'WhiteBread({self.nutrition_facts})'

    def __repr__(self):
        return f'WhiteBread({self.nutrition_facts})'


class BlackBread(Bake):
    def __str__(self):
        return f'BlackBread({self.nutrition_facts})'

    def __repr__(self):
        return f'BlackBread({self.nutrition_facts})'


class CupCake(Bake):
    def __str__(self):
        return f'BlackBread({self.nutrition_facts})'

    def __repr__(self):
        return f'BlackBread({self.nutrition_facts})'


class Croissant(Bake):
    def __str__(self):
        return f'BlackBread({self.nutrition_facts})'

    def __repr__(self):
        return f'BlackBread({self.nutrition_facts})'
