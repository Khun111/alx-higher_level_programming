#!/usr/bin/python3
'''Module a function that checks if the object is an instance of \
a class that inherited (directly or indirectly) from the specified class'''


def inherits_from(obj, a_class):
    '''A function that checks if the object is an instance of a class\
that inherited (directly or indirectly) from the specified class'''
    return issubclass(type(obj), a_class) if type(obj) != a_class else False
