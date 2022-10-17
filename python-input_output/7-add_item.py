#!/usr/bin/python3
""" module imports two functions and execute """

from os import path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists("add_item.json") is False:
    save_to_json_file([], "add_item.json")
_list = load_from_json_file("add_item.json")

for element in range(1, len(argv)):
    _list.append(argv[element])
save_to_json_file(_list, "add_item.json")
