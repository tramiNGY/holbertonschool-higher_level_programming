#!/usr/bin/python3
'''
This module contains one class Student
'''


class Student:
    """Defines students informations"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        filteredinfo = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                filteredinfo[key] = value
        return filteredinfo

    def reload_from_json(self, json):
        if json is None:
            return self.__dict__
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
        return self
