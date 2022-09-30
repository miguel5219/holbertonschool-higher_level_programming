#!/usr/bin/python3
"""define square class"""


class Square:
    """ class with the size attribute and error messages """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be and integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
