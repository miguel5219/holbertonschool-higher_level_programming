#!/usr/bin/python3
"""
print square
function that prints a square with the character #
"""


def print_square(size=1):

    """the function that defines the size of the square"""

    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)