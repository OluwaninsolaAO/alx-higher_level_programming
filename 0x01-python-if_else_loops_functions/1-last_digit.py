#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = str(number)
lastdigit = int(numstr[-1])
if lastdigit > 5:
    print(f"Last digit of {number} is {numstr[-1]} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number} is {numstr[-1]} and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(f"Last digit of {number} is\
 {numstr[-1]} and is less than 6 and not 0")
