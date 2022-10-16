#!/usr/bin/python3
"""
define module
"""

import json

def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text
    file, using a json representation
    """

    with open(filename, 'w') as wf:
        wf.write(jason.dumps(my_obj))
