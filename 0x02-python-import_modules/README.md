# 0x02 Python - Import & Modules

__Project Descriptor:__ Python provides access to built in modules and
packages, which users can import into their programmes at runtime. The same
goes for user's own custom modules and pakages. This section explores how
module import works, its features, limitations, and lots more.



## speak.py

```
#!/usr/bin/python3
import sys

def speak(words):
	print(words)

if __name__ == '__main__':
	speak(sys.argv[1])
```
## main.py
```
#!/usr/bin/python3
from speak import speak as say

say("Hi Mum!")
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
