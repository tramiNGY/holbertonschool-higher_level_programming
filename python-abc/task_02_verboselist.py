#!/usr/bin/python3
'''
This module contains one class VerboseList
'''


class VerboseList(list):
    """Inherited class from list built-in class"""
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        count = len(x)
        super().extend(x)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")
        
    def pop(self, index=-1):
        popped_item = self[index]
        super().pop(index)
        print(f"Popped [{popped_item}] from the list.")
        return popped_item
