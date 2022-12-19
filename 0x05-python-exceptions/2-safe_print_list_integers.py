#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Safe print all integers in a given list"""

    return_value = 0;
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            return_value += 1
        except (TypeError, ValueError):
            pass
        except IndexError:
            raise
    print("")
    return return_value
