#!/usr/bin/python3
'''
This module contains one class BaseGeometry and inherited class Rectangle
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherited class of Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
