#!/usr/bin/python3
import random
number = random.randint(-100000, 10000)
temp = str(number)
num = int(temp[-1])
str = 'Last digit of ' + temp + ' is ' + str(num)
if number > 5:
    str = str + ' and is greater than 5'
elif number == 0:
    str = str + ' and is 0'
elif number < 6 and num != 0:
    str = str + ' and is less than 6 and not 0'
print(str)
