#!/usr/bin/env python3
"""Module that defines a custom object with pickle serialization."""

import pickle


class CustomObject:
    """Custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current object instance to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
