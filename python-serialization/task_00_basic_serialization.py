#!/usr/bin/env python3
"""Basic serialization: save a dict to JSON and load it back."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file (overwrites)."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return it as a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
