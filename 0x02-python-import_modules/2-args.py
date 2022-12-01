#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    argv = sys.argv

    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        i = 1
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1
    else:
        print("{} arguments:".format(len(argv) - 1))
        i = 1
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1
