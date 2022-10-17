#!/usr/bin/python3
""" define class method """


class Student:
    """ define Student class """

    def __init__(self, first_name='', last_name='', age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns:
                    decitionary reprersentation of a student instance """
        return self.__dict__
