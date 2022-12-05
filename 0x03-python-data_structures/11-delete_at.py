#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete from my_list on the index idx"""

    if idx < 0 or idx >= len(my_list):
        return my_list

    del(my_list[idx])

    return my_list
