#!/usr/bin/python3
""" module contains the class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class represents a square inherits from rectangle

    attributes:
        width: the size of the square
        height: the size of the square
        x: the x coordinate of the square
        y: the y coordinate of the square
        id: identifier of the square
    """


    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """ give an argument to each attribute

        attributes:
            args: contains the attributes to be
            updates in the following order

        kwargs: a dictionary with the name of the
        attrs as keys and the values to change
        associated
        """

        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}" \
                f" - {self.width}"
