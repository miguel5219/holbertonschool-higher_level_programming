#!/usr/bin/python3
def uppercase(str):
    letter = 0
    while letter < len(str):
        _letter = ord(str[letter])
        if _letter > 96 and _letter < 123:
            _letter -= 32
        print(chr(_letter), end='')
        letter += 1
    print()
    return True

