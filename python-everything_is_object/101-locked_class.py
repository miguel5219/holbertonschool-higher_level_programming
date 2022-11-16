#!/usr/bin/python3
""" this module contains the class LockedClass """


class LockedClass:
    """ class only allows to assign attributes with
    the name first_name """

    __slots__ = ['first_name']
