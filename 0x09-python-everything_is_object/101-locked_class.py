#!/usr/bin/python3
'''Module for Locked Class'''


class LockedClass:
    '''Only allow the first_name attr'''
    __slots__ = ['first_name']
