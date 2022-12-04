#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for x in range(len(my_string)):
        if not my_string[x] in ['c', 'C']:
            new_string = new_string + my_string[x]
    return new_string
