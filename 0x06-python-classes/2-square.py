#!/usr/bin/python3
'''Define a square class'''


class Square():
    '''Represent the square.'''
    def __init__(self, size=0):
        '''Instantiate the class.
        Args:
            size: Size of the square.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
