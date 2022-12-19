# 0x05 Python - Python - Exceptions

__Project Descriptor:__ Exceptions are cool way of handling errors
that occurs during runtime in a python programme.

This section explores in details how to handle errors that occured
at runtime using try...except blocks.

```
#!/usr/bin/python3
while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops! That was no valid number")
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
