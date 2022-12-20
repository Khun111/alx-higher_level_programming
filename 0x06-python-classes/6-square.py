#!/usr/bin/python3
'''Define a square class.'''


class Square:
    '''Represents a square class.'''
    def __init__(self, size=0, position=(0, 0)):
        '''Instantiate the class.
        Args:
            size: Size of the square.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        try:
            self.__position = position
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')

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

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        try:
            self.__position == value
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return (self.__size ** 2)
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('_' * self.__position[0], end='')
                print('#' * self.__size)
