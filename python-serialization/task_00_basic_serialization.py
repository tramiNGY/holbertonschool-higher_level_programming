#!/usr/bin/python3
'''
This module serializes a Python dictionary to a JSON file
and deserailizes the JSON file to recreate the python dictionary
'''
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
