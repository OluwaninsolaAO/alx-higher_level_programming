#!/usr/bin/python3
"""
A simple pyhton programme that writes into a file
in Append Mode.
- Creates the file if it doesn't exist.
- If the file exist but not empty, appends to the
end of the file
- outputs the total number of characters written
into the file
"""


def append_write(filename="", text=""):
    """
    Creates a file with ``filename`` is it doesn't
    exists and append ``text`` as the content to the
    created file.
    Returns the total number of characters written to
    ``filename``.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
