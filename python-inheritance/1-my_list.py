#!/usr/bin/python3
"""Module that defines a list subclass."""


class MyList(list):
    """A custom list class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
