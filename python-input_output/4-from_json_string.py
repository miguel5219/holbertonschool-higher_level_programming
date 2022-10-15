#!/usr/bin/python3
""" define module """


import json


def from_json_string(my_str):
    """ returns: object represented by a json string """

    return json.loads(my_str)
