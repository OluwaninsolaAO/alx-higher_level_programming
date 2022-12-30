# 0x07 Python - Test-driven development

__Project Descriptor:__ Testing a programme during or after development is an
excellent way to catch bugs and notice some hidden errors in a programme.
Python provides multiple options to automate testing during development
-- Doctest and Unittest. Each of these types will be explored in this section.


```
#!/usr/bin/python3
def multiply(a, b):
   """return a * b
   >>> multiply(20, 5)
   100
   >>> multiply('a', 3)
   'aaa'
   """
   return a * b
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
