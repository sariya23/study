from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Абстрактный класс, представляющий хранилище(холодильник, склад).
    """
    def __init__(self, capacity: int=10):
        self.storage = [None] * capacity
        self.capacity = capacity

    def __len__(self):
        return len(self.storage)

    def __getitem__(self, item):
        key = self.__check_key(item)
        return self.storage[key]

    def __contains__(self, item):
        return item in self.storage

    def __iter__(self):
        yield from self.storage

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        key = self.__check_key(key)
        del self.storage[key]

    def __str__(self):
        return f'{self.storage}'

    def __check_key(self, key: int) -> int:
        if not isinstance(key, int):
            raise TypeError('Index must be integer')
        if key < 0 or key >= len(self.storage):
            raise IndexError('Incorrect index')
        return key