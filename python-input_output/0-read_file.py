#!/usr/bin/python3
"""
this method define reads a file
"""


def read_file(filename=""):
    """
    args:
        filename: name of file
    """
    with open(filename, encoding='utf-8') as rf:
        for line in rf:
            print(line, end='')
