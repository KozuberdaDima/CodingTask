"""This program converts a string integer value to a number format.

The application utilizes class NumberFormatter and method parseInt
that has input param string and returns an integer value.

Sample: “123345” -> 123345, “-123345” -> -123345, “+1” -> 1.
"""

# string = '2321'


class NumberFormatter():

    @staticmethod
    def parseInt(string):
        if isinstance(string, str):
            if 2 <= len(string) <= 2 ** 32 - 1:
                try:
                    integer = int(string)
                    return integer
                except ValueError:
                    print("Error! Input string must be a negative or positive string integer value.")
            else:
                raise Exception('Error! Length of the input string is not in interval 2 ≤ |s| ≤ 2^32-1.')
        else:
            raise TypeError('Error! Input value type is not a string.')


# print(NumberFormatter.parseInt(string) if NumberFormatter.parseInt(string) is not None else '')
