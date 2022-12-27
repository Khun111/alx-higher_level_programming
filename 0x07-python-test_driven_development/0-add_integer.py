#!/usr/bin/python3
'''Module for the add integer function'''
def add_integer(a, b=98):
    '''Funtion adds two integers'''
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))