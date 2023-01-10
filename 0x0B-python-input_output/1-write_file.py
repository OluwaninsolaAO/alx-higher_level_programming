#!/usr/bin/python3
"""
A simple programme that write into a file
- Create new file if it doesn't already exist
- Overwrite the contents if it already exist
"""


def write_file(filename="", text=""):
    """
    ``write_file`` creates a file using ``filename`` and
    writes ``text`` as its content.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
