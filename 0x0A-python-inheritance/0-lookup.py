#!/usr/bin/python3
'''Module for a function that returns the list\
of available attributes and methods of an object'''


def lookup(obj):
    '''a function that returns the list of\
        available attributes and methods of an object'''
    return (dir(obj))
