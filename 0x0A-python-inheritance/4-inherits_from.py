#!/usr/bin/python3
'''Module a function that checks if the object is an instance of \
a class that inherited (directly or indirectly) from the specified class'''


def inherits_from(obj, a_class):
    '''A function that checks if the object is an instance of a class\
that inherited (directly or indirectly) from the specified class'''
    return isinstance(obj, a_class) if not isinstance(obj, a_class) else False
