#!/usr/bin/python3
import sys

if __name__ == "__main__":

    _len = len(sys.argv) - 1

    if _len > 1:
        print("{} arguments:".format(_len))
    elif _len == 1:	
        print("{} arguments:".format(_len))
    else:
        print("{} arguments:".format(_len))

    for i in range(1, _len + 1):
        print("{}: {}".format(i, sys.argv[i]))
