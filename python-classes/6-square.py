#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """square with error messages with attributes"""

    def __init__(self, size=0, position=(0, 0)):

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                for x in range(self.__size):
                    print("#", end="")
                print()

    def area(self):
        return (self.__size**2)
