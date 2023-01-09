#!/usr/bin/python3
'''Module for empty class BaseGeometry'''


class BaseGeometry:
    '''Geometry Class for defining shapes'''

    def area(self):
        '''Function that raises exception when area is not implemented'''
        raise Exception('area() is not implemented')
