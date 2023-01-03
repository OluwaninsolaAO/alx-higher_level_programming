# 0x09 Python - Everything is object

__Project Descriptor:__ This section explores the fact that in python
everything is object, and debunks the stereo types of how variables
declaration and assignments works in python compared to languages like
C. Mutable and Immutable Objects are everywhere in python and assignments
is often done by refrence and not by value in python.


```
>>> a = "banana"
>>> b = a
>>> b = "apple"
>>> a
'banana'
>>> b
'apple'

>>> a = [1, 2, 3]
>>> b = a
>>> b[0] = 5
>>> a
[5, 2, 3]
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
