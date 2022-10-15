#!/usr/bin/python3
"""
method that writes in a file
"""


def write_file(filename="", text=""):
    """
    args:
        filename: name of file
        text: text to attach
    """
    with open(filename, 'w', encoding='utf-8') as rf:
        return rf.write(text)
