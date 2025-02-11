#!/usr/bin/python3
'''
This module contains one function convert_csv_to_json
'''
import csv
import json


def convert_csv_to_json(csv_filename):
    """converts Comma Seperated Value to JSON format"""
    try:
        data = []
        with open(csv_filename, 'r', encoding="utf-8") as cvsf:
            cvsReader = csv.DictReader(cvsf)
            for rows in cvsReader:
                data.append(rows)

        with open("data.json", 'w', encoding="utf-8") as jsonf:
            json.dump(data, jsonf)

        return True

    except Exception:
        return False
