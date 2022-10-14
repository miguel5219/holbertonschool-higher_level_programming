#!/usr/bin/python3
"""module contains the function is_same_class"""


def is_same_class(obj, a_class):
    """
    check if instance
    attributes:
        obj (object): the object to check
        a_class (class): the class it is supossed to belong

    Returns: returns True if the object is exactly an instance of the
    specified class; otherwise return False
    """
    return (issubclass(a_class, obj.__class__))
