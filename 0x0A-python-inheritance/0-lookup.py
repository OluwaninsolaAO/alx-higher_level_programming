#!/usr/bin/python3
"""
A simple programme that returns a list of available
attributes and methods available in an object.
"""


def lookup(obj):
    return dir(obj)
