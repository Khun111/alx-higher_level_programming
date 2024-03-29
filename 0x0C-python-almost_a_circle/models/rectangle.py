#!/usr/bin/python3
'''Module for Rectangle class that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle case that inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiation for class instances'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Get value using tge property decorator'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set value using the property decorator'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Get value using the property decorator'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set value using the property decorator'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''Get value using the property decorator'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set value using the property decorator'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Get value using the property decorator'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set value using the property decorator'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Method that returns the area value of the Rectangle instance.'''
        return self.__width * self.__height

    def display(self):
        '''Method that prints in stdout the\
Rectangle instance with the character'''
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        '''Method for string representation of Rectangle class'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        '''Method that assigns an argument to \
each attribute using args and kwargs'''
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                if type(args[1]) != int:
                    raise TypeError('width must be an integer')
                if args[1] <= 0:
                    raise ValueError('width must be > 0')
                self.__width = args[1]
            if len(args) > 2:
                if type(args[2]) != int:
                    raise TypeError('height must be an integer')
                if args[2] <= 0:
                    raise ValueError('height must be > 0')
                self.__height = args[2]
            if len(args) > 3:
                if type(args[3]) != int:
                    raise TypeError('x must be an integer')
                if args[3] < 0:
                    raise ValueError('x must be >= 0')
                self.__x = args[3]
            if len(args) > 4:
                if type(args[4]) != int:
                    raise TypeError('y must be an integer')
                if args[4] < 0:
                    raise ValueError('y must be >= 0')
                self.__y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'width':
                    if type(v) != int:
                        raise TypeError('width must be an integer')
                    if v <= 0:
                        raise ValueError('width must be > 0')
                if k == 'height':
                    if type(v) != int:
                        raise TypeError('height must be an integer')
                    if v <= 0:
                        raise ValueError('height must be > 0')
                if k == 'x':
                    if type(v) != int:
                        raise TypeError('x must be an integer')
                    if v < 0:
                        raise ValueError('x must be >= 0')
                if k == 'y':
                    if type(v) != int:
                        raise TypeError('y must be an integer')
                    if v < 0:
                        raise ValueError('y must be >= 0')
                setattr(self, k, v)

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Rectangle'''
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width}
