#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    if len(my_list) == 0:
        return (0)
    for row in my_list:
        score += (row[0] * row[1])
        weight += row[1]
    return (score / weight)
