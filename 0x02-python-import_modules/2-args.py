#!/usr/bin/python3

if __name__ == "___main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("{:d} arguments.".format(count))
    elif count == 1:
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))
    for i in range(1, count):
        print("{:d}: {:s}".format(i + 1, sys.arg[i + 1]))
