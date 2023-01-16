#!/usr/bin/python3
'''Module for Square class that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Instantiation for square values'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[{self.__class__.__name__}]\
 ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        '''Get value using the property decorator'''
        return self.width

    @size.setter
    def size(self, value):
        '''Set value using the property decorator'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Method that assigns an argument to \
each attribute using args and kwargs'''
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Rectangle'''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y, }
