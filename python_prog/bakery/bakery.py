class Bakery:
    """
    Класс представляет пекарню. В зависимости
    от размера пекарни (small, medium, big) меняется
    количество персонала и хранилищ.

    В маленькой пекарне 1 холодильник, 1 склад,
    1 повар, 1 кассир.

    В средней пекарне 2 холодильника, 2 склада,
    2 повара, 2 кассира.

    В большой пекарне 4 холодильника, 4 склада,
    3 повара, 3 кассира.
    """
    def __init__(self, name: str, size: str) -> None:
        """
        :param name: Название пекарни.
        :param size: Размер пекарни. Влияет на количество хранилищ и
        персонала
        """
        pass

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
    
