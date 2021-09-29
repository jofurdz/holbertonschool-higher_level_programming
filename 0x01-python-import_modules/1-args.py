#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argc = len(sys.argv) - 1

if argc == 0:
    print("{:d} arguments.".format(0, sys.argv[argc]))
elif argc == 1:
    print("{:d} argument:".format(1))
else:
    print("{:d} arguments:".format(argc))

for x in range(1, argc + 1):
    print("{:d}: {}".format(x, sys.argv[x]))
