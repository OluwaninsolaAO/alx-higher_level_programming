# 0x0A Python Inheritance

__Project Descriptor:__ Inheritance in OOP gives the abily to create a
real world relationships between class objects in python. A as a class
can inherit from another, or even multiple classes. This kind of
relationship is described to be a parent-class and sub-class relationship,
where a sub-class is declared to inherit the properties of the parent class.

Python inheritance is explored in this section of the project.


```
#!/usr/bin/python3
"""A simple instance of inheritance demonstrated"""


class Base():
	"""
	Parent class, assigned unique id to all members
	of the class
	"""

	id = 0
	def __init__(self):
		Base.id += 1
		self.id = Base.id

class User(Base):
	"""
	User is defined to be a sub class of the class Base
	hence, providing access to call on the __init__ function
	from the class Base using the ``super()`` function
	"""

	def __init__(self):
		super().__init__()
	
	def user_id(self):
		print("User Unique ID is: {}".format(self.id))
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
