#!/usr/bin/python3
"""
A simple class that inherits from list
"""


class MyList(list):
    """
    This class extends the class list to add
    ``print_sorted`` method for printing a sorted
    list.
    """
    def print_sorted(self):
        """
        This method sort the list then print without
        overwiriting the original list.
        """
        print(sorted(self))
