#!/usr/bin/python3
'''
This module contains one class Animal
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    """This class handles animal objects"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass of Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass of Animal"""
    def sound(self):
        return "Meow"
