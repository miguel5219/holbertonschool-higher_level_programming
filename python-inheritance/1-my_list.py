#!/usr/bin/python3
"""
Definie subclass
"""


class MyList(list):
    """method that prints the list, but sorted"""
    def print_sorted(self):
        """returns: list printed"""
        return (print(sorted(self)))
