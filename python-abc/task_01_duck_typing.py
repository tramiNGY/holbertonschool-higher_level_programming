#!/usr/bin/python3
'''
This module contains one abstract class Shape
'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """This class defines geometrical shapes"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """This class is inherited from Shape"""
    def __init__(self, radius=0):
        if radius < 0:
            self.__radius = 0
        else:
            self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """This class is inherited from Shape"""
    def __init__(self, width=0, height=0):
        if width < 0:
            self.__width = 0
        if height < 0:
            self.__height = 0
        else:
            self.__width = width
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return self.__width * 2 + self.__height * 2


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
