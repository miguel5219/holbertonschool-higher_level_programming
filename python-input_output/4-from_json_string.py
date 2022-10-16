#!/usr/bin/python3
""" this module contains the
    function from_json_string()
"""


import json


def from_json_string(my_str):
    """ returns: object represented by a json string """

    return json.loads(my_str)
