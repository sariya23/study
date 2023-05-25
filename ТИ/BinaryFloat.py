from collections import namedtuple


class FloatBinary:
    """
    A class represent executor which convert float number to binary
     Attributes
    ----------
    None

    Methods
    -------
    to_binary(number)
    _get_frac(number)
    _get_sign(binary_string)
    _get_order(binary_string)
    _get_mantissa(binary_string)
    _calc_binary_int(integer)
    _calc_binary_float(fractional)
    convert_to_integer(binary_string_number)
    """

    def to_binary(self, number: float | int) -> str:
        """
        convert float number with base 10 to binary form
        :param number: float | int number which convert to binary form
        :return: str binary number
        """
        flag = False
        if number < 0:
            number = -number
            flag = True
        integer_part, fractional_part = int(number), self._get_frac(number)
        integer, fractional = self._calc_binary_int(integer_part), self._calc_binary_float(fractional_part)
        return f'{integer}.{fractional}' if not flag else f'-{integer}.{fractional}'

    def _get_frac(self, number: float) -> float:
        """
        Get float number in base 10 and return fractional part of it
        :param number: float number
        :return: return only fractional part of it number
        """
        integer = int(number)
        return number - integer

    def _calc_binary_int(self, integer: int) -> str:
        """
        Get int part of float number in 10 base and return it in binary form
        :param integer: integer part of number
        :return: return binary form of int part
        """
        return bin(integer)[2:]

    def _calc_binary_float(self, fractional: float) -> str:
        """
        Get frac part of number and return it in binary form
        :param fractional: fractional part of number
        :return: return fractional part of number in binary form
        """
        integer = 0
        res = ''

        while fractional != 0:
            fractional *= 2
            res += str(int(fractional - self._get_frac(fractional)))

            if fractional >= 1:
                fractional -= int(fractional)

        return res

    def convert_to_integer(self, binary_string_number):
        """
        Get float binary number and return it in base 10
        :param binary_string_number: float binary number
        :return: return integer number from binary form
        """
        flag = False
        if '-' in binary_string_number:
            flag = True
            binary_string_number = binary_string_number.replace('-', '')

        binteger_part, bfraction_part = binary_string_number.split('.')
        iinteger_part = int(binteger_part, 2)
        ifraction_part = 0

        for i in range(len(bfraction_part)):
            if bfraction_part[i] == '1':
                ifraction_part += 2 ** -(i + 1)

        return ifraction_part + iinteger_part if not flag else -(ifraction_part + iinteger_part)

    def _get_order(self, binary_string):
        binary_string = binary_string.replace('-', '')

        if self.convert_to_integer(binary_string) >= 1:
            index_dot = binary_string.index('.')
            return bin(64 + index_dot)[2:]
        else:
            index_dot = binary_string.index('.')
            order = 0
            while binary_string[0] != '1':
                binary_string = binary_string[1:]
                order += 1

            return order

    def _get_mantissa(self, binary_string):
        binary_string = binary_string.replace('-', '')

        if self.convert_to_integer(binary_string) >= 1:
            index_dot = binary_string.index('.')
            binary_string = binary_string.replace('.', '')
            return binary_string
        else:
            index_dot = binary_string.index('.')
            binary_string = binary_string.replace('.', '')
            return binary_string[index_dot:]

    def _get_sign(self, binary_string):
        if self.convert_to_integer(binary_string) >= 0:
            return '0'
        return '1'

    def get_note(self, binary_string):
        sign = self._get_sign(binary_string)
        order = self._get_order(binary_string)
        mantissa = self._get_mantissa(binary_string)

        return f'{sign} {order} {mantissa}'


if __name__ == '__main__':
    exe = FloatBinary()

    number1 = -26.28125
    binary_number1 = exe.to_binary(number1)

    with open('log.txt', 'w+', encoding='utf-8') as f:
        print(f'Number {number1}:', file=f)
        print(f'Number {number1} in 2 base: {binary_number1}', file=f)
        print(f'Check:\n\t {number1} -> {binary_number1} -> {exe.convert_to_integer(binary_number1)}'
              f' -- Result: {number1 == exe.convert_to_integer(binary_number1)}', file=f)
        print(exe.get_note(binary_number1), file=f)
        print('\n', file=f)

        number2 = 0.1875
        binary_number2 = exe.to_binary(number2)
        print(f'Number {number2}:', file=f)
        print(f'Number {number2} in 2 base: {binary_number2}', file=f)
        print(f'Check:\n\t {number2} -> {binary_number2} -> {exe.convert_to_integer(binary_number2)}'
              f' -- Result: {number2 == exe.convert_to_integer(binary_number2)}', file=f)
        print(exe._get_order(binary_number2), file=f)

