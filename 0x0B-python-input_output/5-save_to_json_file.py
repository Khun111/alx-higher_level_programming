#!/usr/bin/python3
'''Module for a function that returns the JSON\
representation of an object (string)'''
import json


def save_to_json_file(my_obj, filename):
    '''A function that returns the JSON \
                   repesentation of an object (string)'''
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
