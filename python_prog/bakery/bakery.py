from fruits import Banana
from validators.validator_size import CorrectSize
from storages.fridges import SmallFridge, MediumFridge, BigFridge
from storages.storerooms import SmallStoreroom, MediumStoreroom, BigStoreroom
from persons import Boss, Cook, Cashier


class Bakery:
    """
    Класс представляет пекарню. В зависимости
    от размера пекарни (small, medium, big) меняется
    количество персонала и хранилищ.

    В маленькой пекарне 1 маленький холодильник, 1 склад, 1 босс
    1 повар, 1 кассир.

    В средней пекарне 1 средний холодильника, 1 средний склад, 1 босс
    2 повара, 2 кассира.

    В большой пекарне 1 большой холодильник, 1  большой склад, 1 босс
    3 повара, 3 кассира.
    """

    size = CorrectSize()

    def __init__(self, name: str, size: str) -> None:
        """
        :param name: Название пекарни.
        :param size: Размер пекарни. Влияет на количество хранилищ и
        персонала
        """
        self.name = name
        self.size = size

        if size == 'small':
            self.storage = SmallStoreroom()
            self.fridge = SmallFridge()
            self.boss = Boss('Adrew', 'Ivanov')
            self.cashier = Cashier('Sergey', 'Pop')
            self.cook = Cook('Fedya', 'Senya')

        elif size == 'medium':
            self.storage = MediumStoreroom()
            self.fridge = MediumFridge()
            self.boss = Boss('Adrew', 'Ivanov')
            self.cashier1 = Cashier('Sergey', 'Pop')
            self.cashier2 = Cashier('Ana', 'Pop')
            self.cook1 = Cook('Fedya', 'Senya')
            self.cook2 = Cook('Maks', 'Lavrov')

        else:
            self.storage = BigStoreroom()
            self.fridge = BigFridge()
            self.boss = Boss('Adrew', 'Ivanov')
            self.cashier1 = Cashier('Sergey', 'Pop')
            self.cashier2 = Cashier('Ana', 'Pop')
            self.cashier3 = Cashier('Dima', 'Pop')
            self.cook1 = Cook('Fedya', 'Senya')
            self.cook2 = Cook('Maks', 'Lavrov')
            self.cook3 = Cook('Victor', 'Barinov')

    def __str__(self):

        res = f'{self.name}\n\n'

        for name, value in self.__dict__.items():
            if name in 'boss' or name in 'cashier' or name in 'cook':
                res += f'{value}\n'

        return res

    @classmethod
    def create_small_bakery(cls, name: str) -> 'Bakery':
        """
        Создает и возвращает маленькую пекарню
        """
        return cls(name, size='small')

    @classmethod
    def create_medium_bakery(cls, name: str) -> 'Bakery':
        """
        Создает и возвращает среднюю пекарню
        """
        return cls(name, size='medium')

    @classmethod
    def create_big_bakery(cls, name: str) -> 'Bakery':
        """
        Создает и возвращает большую пекарню
        """
        return cls(name, size='big')

    def GeT_mOrE_moNEY(self, new_size: str) -> 'Bakery'':
        """
        Возвращает пекарню нового размера.
        """
        return type(self)(self.name, new_size)

