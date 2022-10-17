#!/usr/bin/python3
""" module imports two functions and execute """


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_obj_json = "add_item.json"

try:
    _list = load_from_json_file(file_obj_json)
except FileNotFoundError:
    _list = []

for element in sys.argv[1:]:
    _list.append(element)

save_to_json_file(_list, file_obj_json)
