#!/usr/bin/python3

# islower - chechk lowercase character
# @c: character to check
# Return: true if c is lowercase, false is otherwise

def islower(c):
    if (ord(c) >= 96 and ord(c) <= 123):
        return True
    return False
