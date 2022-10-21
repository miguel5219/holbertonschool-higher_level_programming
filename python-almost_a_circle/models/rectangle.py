#!/usr/bin/python3
""" module contains the class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ class represents a rectangle and inherits from Base

    attributes:
        width: the width of the rectangle
        height: the height of the rectangle
        x: the x coordinate of the rectangle
        y: the y coordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
