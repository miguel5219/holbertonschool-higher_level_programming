#!/usr/bin/python3
""" class base """
import json
import os


class Base:
    """ this class handles the instance attribute
        id for other classes to to save code

        attributes:
            __nb_objects: couter for the number of
            objects created from this class
            id: the id user wants to assings to the
            objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation
            of list_dictionaries

            attributes:
                list_dictionaries: list with the dictionary
        """

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation
        of list_objs to a file

        attributes:
            list_objs: list with objects
        """

        result = []
        if list_objs is not None:
            result = [elem.to_dictionary() for elem in list_objs]
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string

        attributes:
            json_string: a string representing a list of 
            dictionaries
        """

        if json_string is None:
            return []
        return json.loads(json_string)
