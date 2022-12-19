#!/usr/bin/python3
def safe_print_integer_err(value):
    """Safely print integer with  error handling"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: ", err)
        return False
