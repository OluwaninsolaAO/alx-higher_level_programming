#!/usr/bin/python3
def safe_print_division(a, b):
    """Safe print a division of two integers
    While suppressing all errors!"""

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
