#!/usr/bin/python3
'''
This module contains one class BaseGeometry and inherited class Rectangle
'''


class BaseGeometry:
    """Class for basic geometry calculation"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Inhereted class of BaseGeometry"""
    def __init__(self, width=None, height=None):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
