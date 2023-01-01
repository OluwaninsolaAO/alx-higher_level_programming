#!/usr/bin/python3
"""
A function that prints a text with 2 new lines after each
of the following characters '.', '?' and ':'.
"""

def text_indentation(text):
    """
    ``text```: the parsed text (required)
    Only string is acceptable arguement to this function
    """
    indents = ['.', '?', ':']
    space_lock = 0

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in text:
        if i == ' ' and space_lock == 1:
            continue
        else:
            space_lock = 0

        if i in indents:
            print(i, end="\n\n")
            space_lock = 1
        else:
            print(i, end="")
