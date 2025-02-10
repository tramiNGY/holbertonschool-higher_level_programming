#!/usr/bin/python3
'''
This module contains one function to_json_string
'''
import json


def to_json_string(my_obj):
    """Returns representation of an object"""
    return json.dumps(my_obj)
