#!/usr/bin/python3
""" define module """


import json


def to_json_string(my_obj):
    """returns: json representation of the object """

    return json.dumps(my_obj)
