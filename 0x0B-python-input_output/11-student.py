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

    def to_json(self, attrs=None):
        '''Method that retrieves a dictionaryrepresentation of a Student
        '''
        if isinstance(attrs, list) and all(isinstance(ele, str)
                                           for ele in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Method that replaces all attributes of the Student instance
        '''
        for key, val in json.items():
            setattr(self, key, val)
