#!/usr/bin/python3
'''Module for Rectangle Class'''


class Rectangle:
    '''Class to define a Rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = []
        for i in range(self.__height):
            if i != self.__height - 1:
                shape.append(self.__width * str(self.print_symbol) + '\n')
            else:
                shape.append(self.__width * str(self.print_symbol))
        return (''.join(shape))

    def __repr__(self):
        shapeinst = 'Rectangle(' + str(self.__width) + \
            ' , ' + str(self.__height) + ')'
        return shapeinst
    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
