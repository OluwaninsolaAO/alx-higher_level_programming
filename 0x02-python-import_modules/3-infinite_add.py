#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    argv = sys.argv
    arg_len = len(argv) - 1

    if arg_len == 0:
        print("{}".format('0'))
    else:
        sum = 0
        n = 1
        while n <= arg_len:
            sum += int(argv[n])
            n += 1
        print("{}".format(sum))
