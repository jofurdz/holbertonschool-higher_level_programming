#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = (number * -1) % 10 * -1
else:
    lastDigit = number % 10
s1 = "Last digit of"
s2 = "and is greater than 5"
s3 = "and is 0"
s4 = "and is less than 6 and not 0"
if lastDigit > 5:
    print("{:s} {:d} is {:d} {:s}".format(s1, number, lastDigit, s2))
if lastDigit == 0:
    print("{:s} {:d} is {:d} {:s}".format(s1, number, lastDigit, s3))
if (lastDigit < 6 and lastDigit != 0):
    print("{:s} {:d} is {:d} {:s}".format(s1, number, lastDigit, s4))
