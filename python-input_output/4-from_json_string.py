#!/usr/bin/python3
"""Module that defines a JSON deserialization function."""

import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string."""
    return json.loads(my_str)
