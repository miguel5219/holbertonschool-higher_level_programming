#!/usr/bin/python3
def uppercase(str):
# letter = 0
    for letter in str:
        i = ord(letter)
        _letter = letter
        if i >= 96 and i <= 123:
            _letter = chr(i - 32)
        print("{}".format(_letter), end="")
#letter += 1
    print("{}".format(""))
#return True

