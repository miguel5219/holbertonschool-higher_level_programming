#!/usr/bin/python3
""" define method, returns obj dict """


def class_to_json(obj):
    """ args:
            obj: instance a class
        returns:
            dictionary description
    """
    return obj.__dict__
