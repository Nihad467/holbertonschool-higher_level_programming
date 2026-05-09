#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance."""
        if type(attrs) is list:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs and type(key) is str
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
