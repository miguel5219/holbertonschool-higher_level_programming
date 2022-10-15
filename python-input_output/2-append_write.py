#!/usr/bin/python3
"""
method that appends a line in a file
"""


def append_write(filename="", text=""):
    """
    args:
        filename: name of file
        text: text to attach
        """
    withopen(filename, 'a', encoding='utf-8') as rf:
        return rf.write(text)
