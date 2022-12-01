#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    args = dir(hidden_4)
    args.sort()

    for i in range(len(args)):
        if args[i][0] != '_':
            print("{}".format(args[i]))
