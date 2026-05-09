#!/usr/bin/python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file.

    Return the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
