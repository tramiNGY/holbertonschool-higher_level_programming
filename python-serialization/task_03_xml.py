#!/usr/bin/python3
'''
This module contains 2 functions to serialize
and deserialize using XML
'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize dictionary into XML and saves it to filename"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        sub_element = ET.SubElement(root, key)
        sub_element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """read the XML data from filename and returns a deserialized dictonary"""
    dictionary = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for element in root:
        dictionary[element.tag] = element.text
    return dictionary
