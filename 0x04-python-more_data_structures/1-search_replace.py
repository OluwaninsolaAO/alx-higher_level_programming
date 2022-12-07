#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces search with replace in my_list"""

    return list(map(lambda x: replace if x == search else x, my_list))
