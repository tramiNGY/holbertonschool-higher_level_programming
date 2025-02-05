#!/usr/bin/python3
'''
This module contains mixin classes
'''


class SwimMixin:
    """mixin class for swimming"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """mixin class for flying"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    "Inherited from mixin classes"
    def roar(self):
        print("The dragon roars!")
