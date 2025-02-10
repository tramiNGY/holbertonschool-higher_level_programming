#!/usr/bin/python3
'''
This module adds all arguments to python list and saves to a file
'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    my_list = load_from_json_file("add_item.json")
except Exception:
    my_list = []
args = sys.argv[1:]
my_list.extend(args)
save_to_json_file(my_list, "add_item.json")
