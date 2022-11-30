#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            j = 32
        else:
            j = 0
        print("{:c}".format(ord(i) - j), end="")
    print()
