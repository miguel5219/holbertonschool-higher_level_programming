#!/usr/bin/python3
"""
text indentation
function that prints a text
"""


def text_indentation(text):

    """
    function that prints a text with 2 new lines
    after each ofthese characters: ., ?, and :
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    str_ = ""
    i = 0
    while i < len(text):

        str_ += text[i]
        if text[i] in ['.', '?', ':']:
            print(str_.strip())
            print()
            str_ = ""
        i += 1
    if str_ is not "":
        print(str_.strip(), end="")
