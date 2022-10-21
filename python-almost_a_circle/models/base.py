#!/usr/bin/python3
""" class base """


class base:
    """ this class handles the instance attribute
        id for other classes to to save code 

        attributes:
            __nb_objects: couter for the number of
            objects created from this class
            id: the id user wants to assings to the
            objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
