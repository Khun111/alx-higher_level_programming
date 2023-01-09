#!/usr/bin/python3
'''Module for empty class BaseGeometry'''


class BaseGeometry:
    '''Geometry Class for defining shapes'''

    def area(self):
        '''Function that raises exception when area is not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Function to calidate value entered'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
