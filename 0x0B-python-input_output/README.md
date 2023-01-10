# 0x0B Python Input Output

__Project Descriptor:__ Files creation is quite useful where it will
be a demand to have a reusable data for a programme that can be
preloaded on start or during the execution of the programme itself.

Python Input/Output gives access to couple of functions or methods
on a file object for manipulation. Function such as ```open()```, methods
such as ```write()```, ```writelines()```, ```read()```, ```readline()```
, ```readlines()``` come in very handy and convinient when it comes to file
manipulation in python. This topic is explored in this section of the project.


```
#!/usr/bin/python3
import os

with open("NewTextFile.txt", "w", encoding="utf-8") as f:
	f.write("Awesome Contents\nWith more awesome texts\nEven more!")

with open("NewTextFile.txt", "r", encoding="utf-8") as f:
	print(f.readline())		# Awesome Contents
	f.tell()			# 17
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
