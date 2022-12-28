#!/usr/bin/python3
'''Module for text indentation'''


def text_indentation(text):
    '''Funtion for text indentation

    Args:
        text: string to print
    Raise:
         TypeError if not string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent = False
    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print()
            indent = True
        else:
            if indent and char == ' ':
                continue
            else:
                indent = False
                print(char, end='')
