#!/usr/bin/python3
"""
contains the class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a subclass with parent Rectangle
    """
    def __init__(self, size):
        """
        methodthat validates args and set 
        the as private attributes
        args:
            size: Square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
