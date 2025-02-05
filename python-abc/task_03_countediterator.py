#!/usr/bin/python3
'''
This module contains one class CountedIterator
'''


class CountedIterator:
    """Extends the built-in iterator"""
    def __init__(self, some_iterable, count=0):
        self.__some_iterable = some_iterable
        self.__iterator = iter(some_iterable)
        self.__count = count

    def get_count(self):
        return self.__count

    def __next__(self):
        self.__count += 1
        return next(self.__iterator)
