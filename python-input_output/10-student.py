#!/usr/bin/python3
""" define class method """


class Student:
    """ class """
    def __init__(self, first_name='', last_name='', age=0):
        """ method that assigns public attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns: dictionary representation of studente instance
        note: if attrs is a list ofstrings, only attribute name
            contained in this list must be retrieved.
            otherwise, all attributes must be retrieved
        """

        obj_ = dict()
        if type(attrs) is list:
            for _obj_ in attrs:
                if type(_obj_) is not str:
                    return self.__dict__

                if _obj_ in self.__dict__:
                    obj_[_obj_] = self.__dict__[_obj_]

            return obj_

        return self.__dict__
