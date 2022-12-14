#!/usr/bin/python3
'''Define a square class.'''


class Square:
    '''Represents a square class.'''
    def __init__(self, size=0):
        '''Instantiate the class.
        Args:
            size: Size of the square.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return (self.__size ** 2)
