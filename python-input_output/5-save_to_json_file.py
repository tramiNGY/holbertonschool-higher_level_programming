#!/usr/bin/python3
'''
This module contains one function save_to_json_file
'''
import json


def save_to_json_file(my_obj, filename):
    """Open filename, converts m_obj and writes it in file"""
    json_obj = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json_obj)
