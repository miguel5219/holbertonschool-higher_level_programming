#!/usr/bin/python3
"""
Define subclass rectangle using
BaseGeometry as parent class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass Rectangle with class BaseGeometry
    """
    def __init__(self, width, height):
        """
        attributes:
        width (int): The width of the rectangle
        height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        return: rectangle area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        return: String with information
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
