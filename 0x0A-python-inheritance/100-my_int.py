#!/usr/bin/python3
''' Module for rebel class'''


class MyInt(int):
    '''Rebel class with equality signs inverted'''

    def __eq__(self, value):
        '''Magic method to invert equality'''
        return self.real != value

    def __ne__(self, value):
        '''Magic method to invert inequality'''
        return self.real == value
