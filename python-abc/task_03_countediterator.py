#!/usr/bin/python3
'''
This module contains one class CountedIterator
'''


class CountedIterator:
    """Extends the built-in iterator"""
    def __init__(self, some_iterable):
        self.__some_iterable = some_iterable
        self.__iterator = iter(some_iterable)
        self.__count = 0

    def get_count(self):
        return self.__count

    def __next__(self):
        self.__count += 1
        if self.__count <= len(self.__some_iterable):
            return next(self.__iterator)
        else:
            raise StopIteration("No more items.")
