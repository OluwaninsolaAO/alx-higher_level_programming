#!/usr/bin/python3
def safe_print_integer(value):
    """Safe print integer value"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
