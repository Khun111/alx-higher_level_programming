#!/usr/bin/python3
'''Module for a function that returns the JSON\
representation of an object (string)'''
import json


def to_json_string(my_obj):
    '''A function that returns the JSON representation of an object (string)'''
    return json.dumps(my_obj)
