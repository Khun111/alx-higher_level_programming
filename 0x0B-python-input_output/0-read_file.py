#!/usr/bin/python3
'''Module for a function that reads a text file\
(UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''A function that reads a text file (UTF8) and prints it to stdout'''
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
