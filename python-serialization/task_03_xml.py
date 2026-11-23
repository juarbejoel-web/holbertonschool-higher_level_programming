#!/usr/bin/env python3
"""Serialize and deserialize a dictionary with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file with a <data> root."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Read an XML file and return its content as a dictionary."""
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
