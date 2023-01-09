#!/usr/bin/python3
'''Module for a function that adds new attr to a function'''


def add_attribute(inst, attr, val):
    '''A function that adds new attr to a function'''
    if not hasattr(inst, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(inst, attr, val)
