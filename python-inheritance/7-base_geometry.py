#!/usr/bin/python3
"""
define class called BaseGeometry
"""


class BaseGeometry:
    """
    class with area method
    """
    def area(self):
        """
        raises:
            Exception: area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Args:
            name: name
            value: value

        Raises:
            TypeError: name must be an integer
            ValueError: name must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
