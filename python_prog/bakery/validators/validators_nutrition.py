class CorrectNutrition:
    """
    Дескриптор, проверяющий, что значения БЖУ числа больше нуля.
    """
    def __set_name__(self, owner, attr):
        self._attr = attr

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value < 0:
            raise ValueError('Incorrect value')
        instance.__dict__[self._attr] = value


    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Attribute is not defined')