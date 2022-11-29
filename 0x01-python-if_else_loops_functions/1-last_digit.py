#!/usr/bin/python3
import random
number = random.randint(-100000, 10000)
numstr = str(number)

if number > 5:
    print(f"Last digit of {number} is {numstr[-1]} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {number} and is 0")
elif number < 6 and number != 0:
    print(f"Last digit of {number} is\
 {numstr[-1]} and is less than 6 and not 0")
