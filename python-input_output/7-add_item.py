#!/usr/bin/python3
'''
This module adds all arguments to python list and saves to a file
'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    my_obj = load_from_json_file("add_item.json")
except Exception:
    my_obj = []
arg = sys.argv[1:]
my_obj.extend(arg)
save_to_json_file(my_obj, "add_item.json")
