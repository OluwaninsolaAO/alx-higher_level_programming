# ALX Higher Level Programming


__Project Scope:__ This is programming in high level programming
language - Python.

__Project Details:__ Programming in Python is promised to be fun,
more than C I hoped. Python offers extensive  libraries and uses
less lines of code compared with C. More details about python later.

## Shell scripts at the root directory

### create
> I wrote this script to help me with the repetitive task of creating executable python files,
> start editing the created file with the first line automatically append to the file. The name
> of the file will be passed as second arguement while calling/executing the script.
>
> I named the file create and make it executable, and I use ```vim``` editor, which makes me 
> default the editing of the created script to be opened by ```vim```.
> Calling the script from my sub directories is a bit of work, but still convinient: 
> For example; to create a python file ```main.py``` from any of my sub-directory:
>
> ```$ ../create main.py```

### check
> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle compliant. The_
_choice Style Guide for Python Code._ Checking styles to comply with Pycodestyle could be 
better, I tried to save a few key strokes with the check script, kinda straightforward.
>
>Use case; checking a file ```main.py``` if it is Pycodestyle compliant from any of my 
sub-directory:
>
> ```$ ../check main.py```

### push
> Push is as simple as it is named, this script staged all changes made in the repository,
> create a commit message, and push to remote repository. The commit message was defaulted
> to start with the string "```Task```" meanwhile, I have always use the string "```Task```"
> with the project task number as my commit message for simplicity.
>
> Use case of the push shell script from any of my sub-directory:
>
> ```$ ../push "10: This C task in python project is weird"```

__About Author:__ You can read more about [OluwaninsolaAO](https://www.linkedin.com/in/oluwaninsolaao) on LinkedIn.
