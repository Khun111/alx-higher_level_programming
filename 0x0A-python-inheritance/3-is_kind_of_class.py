#!/usr/bin/python3
'''Module for a function that checks if an\
object is exactly an instanceof a class'''


def is_kind_of_class(obj, a_class):
    '''Function that checks if an object is\
    exactly an instance of a class'''
    return isinstance(obj, a_class)
