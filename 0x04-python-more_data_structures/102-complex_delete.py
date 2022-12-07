#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for k in a_dictionary:
            if a_dictionary[k] == value:
                del a_dictionary[k]
                break
    return (a_dictionary)
