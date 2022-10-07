#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """ definition of class rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """claculates the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)

        return (2 * self.width + 2 * self.height)

    def __str__(self):
        """print method"""
        string_result = ""

        if not self.width or not self.height:
            return (string_result)

        for i in range(self.height):
            string_result += ("#" * self.width) + "\n"
        return (string_result[:-1])

    def __repr__(self):
        """representation of object"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
