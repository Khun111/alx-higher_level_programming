#!/usr/bin/python3
'''Module for a class that defines a student'''


class Student:
    '''A class that defines a student'''

    def __init__(self, first_name, last_name, age):
        '''A function to instantiate the class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Method that retrieves a dictionaryrepresentation of a Student
        '''
        return self.__dict__
