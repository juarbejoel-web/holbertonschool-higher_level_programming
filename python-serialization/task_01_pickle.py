#!/usr/bin/env python3
"""Serialize and deserialize a custom object with pickle."""
import pickle


class CustomObject:
    """A simple object that can be pickled to and from a file."""

    def __init__(self, name, age, is_student):
        """Initialize the object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this instance to a file. Return None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an instance from a file. Return None on failure."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
        except Exception:
            return None
        if not isinstance(obj, cls):
            return None
        return obj
