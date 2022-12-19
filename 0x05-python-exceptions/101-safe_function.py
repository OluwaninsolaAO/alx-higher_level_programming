#!/usr/bin/python3
def safe_function(fct, *args):
    """Safely executes  any functions with error handling"""

    import sys
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
