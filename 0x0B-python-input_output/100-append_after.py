#!/usr/bin/python3
'''Module for a function that inserts a line of text to a file, after\
each line containing a specific string'''


def append_after(filename="", search_string="", new_string=""):
    '''A function that inserts a line of text to a file,\
                after each line containing a specific string
    '''
    writeup = ''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            writeup += line
            if search_string in line:
                writeup += new_string
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(writeup)
