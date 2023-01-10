#!/usr/bin/python3
"""
A simple programme that reads from a file
and prints it to standard output.
"""


import os


def read_file(filename=""):
    """
    ``read_file`` reads a content of a file
    ``filename`` and prints it to standard output.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
