#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    l_len = 0
    for i in range(x):
        try:
            print(f'{my_list[i]}', end='')
            l_len += 1
        except IndexError:
            break
    print()
    return l_len
