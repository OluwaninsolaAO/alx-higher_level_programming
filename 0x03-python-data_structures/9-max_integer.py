#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find in a list a maximum integer value"""

    if not my_list:
        return None
    else:
        max_value = my_list[0]
        for x in my_list:
            if x >= max_value:
                max_value = x
        return max_value
