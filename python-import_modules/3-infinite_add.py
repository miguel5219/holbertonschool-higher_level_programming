#!/usr/bin/python3
import sys

if __name__ == "__main__":

    _len = len(sys.argv) - 1
    a = 0

    for itr in range(1, _len + 1):
        a += int(sys.argv[itr])

    print("{}".format(a))
