#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = my_list[:]
    for i in newl:
        if i == search:
            newl[newl.index(i)] = replace
    return (newl)
