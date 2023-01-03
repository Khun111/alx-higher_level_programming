#!/usr/bin/python3
'''Module for magic_string'''


def magic_string():
    '''magic_string() that returns a string
    “BestSchool” n times the numberof the iteration
    '''
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "BestSchool, " * (magic_string.count - 1) + "BestSchool"
