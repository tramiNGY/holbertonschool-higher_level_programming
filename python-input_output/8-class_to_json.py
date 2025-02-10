#!/usr/bin/python3
'''
This module contains one function class_to_json
'''


def class_to_json(obj):
    """returns the dictionary description with simple data"""
    return obj.__dict__
