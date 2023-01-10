#!/usr/bin/python3
'''Module a function that writes a string at the end of a text filei\
(UTF8) and returns the number of characters added:'''


def write_file(filename="", text=""):
    '''A function that writes a string at the end of a text file (UTF8)\
                and returns the number of characters added:'''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
