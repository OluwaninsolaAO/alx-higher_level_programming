#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list)
    for x in my_list[:lenght]:
        print("{:d}".format(my_list.pop()))
