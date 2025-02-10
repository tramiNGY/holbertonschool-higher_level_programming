#!/usr/bin/python3
'''
This module contains one function from_json_string
'''
import json


def from_json_string(my_str):
    """Returns representation of an object"""
    return json.loads(my_str)
