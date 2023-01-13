#!/usr/bin/python3
'''This Module creates the Base class to handle ids'''


class Base:
    '''Class to handle id attribute of future classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiation for class instances'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
