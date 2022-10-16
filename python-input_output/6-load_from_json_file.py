#!/usr/bin/python3
"""
define module
"""
import json


def load_from_json_file(filename):
    """ module that creates an object from a json file """

    with open(filename, mode='r', enconding='utf-8') as rf:
        return json.load(rf)
