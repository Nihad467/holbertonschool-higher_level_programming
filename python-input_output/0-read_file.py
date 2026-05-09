#!/usr/bin/python3
"""Module that defines a function to read a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
