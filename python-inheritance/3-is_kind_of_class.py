#!/usr/bin/python3
"""define method"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of a_class

    args:
        obj: object to check
        a_class_ class to take a look in

    returns: True if the object is an instance of,
    or if the object is an instance of a class that inherited from, 
    the especified class
    """
    return (isinstance(obj, a_class))
