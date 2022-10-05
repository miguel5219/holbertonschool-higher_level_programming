#!/usr/bin/python3
"""
Integers addition,
function that adds 2 integers
"""


def add_integer(a, b=98):

    """
    function that defines 2 integers
    and return a result
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return(a + b)