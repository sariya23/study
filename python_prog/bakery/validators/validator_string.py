from string import ascii_letters

class CorrectString:
    """
    Дескриптор, проверяющий, что строковые
    значения длиной больше нуля и состоят только из букв.
    """
    def __set_name__(self, owner, attr):
        self._attr = attr


    def __set__(self, instance, value):
        if isinstance(value, str)\
                and len(value) > 0 and\
                all(letter in ascii_letters for letter in value):
            instance.__dict__[self._attr] = value
        else:
            raise ValueError('Incorrect value')


    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Attribute is not defined')