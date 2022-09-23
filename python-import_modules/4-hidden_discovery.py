#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    _list = dir(hidden_4)

    for element in _list:
        if element[0] != "_":
            print("{}".format(element))
