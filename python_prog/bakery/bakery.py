class Bakery:
    """
    Класс представляет пекарню. В зависимости
    от размера пекарни (small, medium, big) меняется
    количество персонала и хранилищ.
    """
    def __init__(self, name: str, size: str) -> None:
        """
        :param name: Название пекарни.
        :param size: Размер пекарни. Влияет на количество хранилищ и
        персонала
        """
        pass

    @classmethod
    def small(cls, name: str):
        return cls(name, size='small')

    @classmethod
    def medium(cls, name: str):
        return cls(name, size='medium')
    
