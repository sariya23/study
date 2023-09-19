from abstract_classes.abstract_fruit import Fruit


class Banana(Fruit):
    def __str__(self):
        return f'Banana({self.nutrition_facts})'

    def __repr__(self):
        return f'Banana({self.nutrition_facts})'


class Lemon(Fruit):
    def __str__(self):
        return f'Lemon({self.nutrition_facts})'

    def __repr__(self):
        return f'Lemon({self.nutrition_facts})'


class Pineapple(Fruit):
    def __str__(self):
        return f'Pineapple({self.nutrition_facts})'

    def __repr__(self):
        return f'Pineapple({self.nutrition_facts})'


class Qiwi(Fruit):
    def __str__(self):
        return f'Qiwi({self.nutrition_facts})'

    def __repr__(self):
        return f'Qiwi({self.nutrition_facts})'


class Grape(Fruit):
    def __str__(self):
        return f'Grape({self.nutrition_facts})'

    def __repr__(self):
        return f'Grape({self.nutrition_facts})'
