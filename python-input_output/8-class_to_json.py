#!/usr/bin/python3
"""Module that defines a class to JSON dictionary function."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization."""
    return obj.__dict__
