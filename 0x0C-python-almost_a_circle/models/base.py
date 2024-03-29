#!/usr/bin/python3
'''This Module creates the Base class to handle ids'''
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Static method that returns the JSON \
string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Classmethod (cls, list_objs): that writes\
the JSON string representation of list_objs to a file'''
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as my_file:
            if list_objs is None:
                my_file.write('[]')
            else:
                dict_li = [inst.to_dictionary() for inst in list_objs]
                my_file.write(cls.to_json_string(dict_li))

    @staticmethod
    def from_json_string(json_string):
        '''Static method that returns the list of \
the JSON string representation json_string:'''
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Classmethod that returns an instance\
with all attributes already set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                c = cls(5, 3)
            else:
                c = cls(5)
            c.update(**dictionary)
        return c

    @classmethod
    def load_from_file(cls):
        '''Classmethod that returns a list of instances'''
        try:
            with open(f'{cls.__name__}.json', 'r') as json_f:
                if not json_f:
                    return []
                loaded_l = Base.from_json_string(json_f.read())
            return [cls.create(**x) for x in loaded_l]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Classmethod (cls, list_objs): that writes\
the JSON string representation of list_objs to a file'''
        with open(f'{cls.__name__}.csv', 'w', newline='') as my_file:
            if list_objs is None or len(list_objs) == 0:
                my_file.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']
                written = csv.DictWriter(my_file, fieldnames=fields)
                [written.writerow(inst.to_dictionary()) for inst in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        '''Classmethod that returns a list of instances'''
        dict_li = []
        try:
            with open(f'{cls.__name__}.csv', 'r') as csv_f:
                if not csv_f:
                    return []
                else:
                    if cls.__name__ == 'Rectangle':
                        fields = ['id', 'width', 'height', 'x', 'y']
                    else:
                        fields = ['id', 'size', 'x', 'y']
                    csv_r = csv.DictReader(csv_f, fieldnames=fields)
                    for row in csv_r:
                        dict_li.append(dict([k, int(row[k])] for k in row))
                return [cls.create(**x) for x in dict_li]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.setup(width=800, height=600)
        turtle.screensize(800, 600)
        turtle.bgcolor("white")

        for rect in list_rectangles:
            turtle.pencolor("blue")
            turtle.penup()
            turtle.setpos(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)

        for square in list_squares:
            turtle.pencolor("green")
            turtle.penup()
            turtle.setpos(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.exitonclick()
