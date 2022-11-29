#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = number % 10

if result == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, result))
elif result > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, result))
elif result < 6 and result > 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, result))
