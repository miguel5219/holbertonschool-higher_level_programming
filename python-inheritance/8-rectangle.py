#!/usr/bin/python3
"""
this module define subclass rectangle using
BaseGeometry as parent class
"""


BaseGeometry = __import___('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this is Subclass Rectangle with class BaseGeometry
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
