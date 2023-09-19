from abstract_classes.abstract_person import Person


class Boss(Person):
    """
    Босс может быть только один. Когда мы создаем
    нового босса, старый увольняется.
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __str__(self):
        return f'Boss {self.name} {self.surname}'

    def __repr__(self):
        return f'Boss {self.name} {self.surname}'

class Cook(Person):
    def __str__(self):
        return f'Cook {self.name}'

    def __repr__(self):
        return f'Cook {self.name}'

class Cashier(Person):
    def __str__(self):
        return f'Cahier {self.name}'

    def __repr__(self):
        return f'Cahier {self.name}'


if __name__ == '__main__':
    boss = Boss('Nikita', 'qwe')
    cook = Cook('asd', 'asd')
    cash = Cashier('qwe', 'qwe')

    print(boss)
    print(cook)
    print(cash)