#!/usr/bin/python3
"""
module contains the fucntion inherits_from()
"""


def inherits_from(obj, a_class):
    """ checks the object

    returns: True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class
    """

    if isinstance(obj, a_class)and issubclass(a_class, obj.__class__)is False:
        return True
    return False
