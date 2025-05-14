#!/usr/bin/env python3
import csv
import json
from task_02_csv import convert_csv_to_json

def display_csv_content(csv_filename):
    """Affiche le contenu du fichier CSV avant la conversion"""
    with open(csv_filename, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        print("CSV Dataset:")
        for row in csv_reader:
            print(row)

def display_json_content(json_filename):
    """Affiche le contenu du fichier JSON après la conversion"""
    with open(json_filename, 'r', encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
        print("\nJSON Dataset:")
        print(json.dumps(data, indent=4, ensure_ascii=False))

def main():
    # Nom du fichier CSV à convertir
    csv_file = "data.csv"
    json_file = "data.json"

    # Affiche le contenu du CSV avant la conversion
    display_csv_content(csv_file)

    # Appel de la fonction pour convertir le fichier CSV en JSON
    convert_csv_to_json(csv_file)

    # Affiche le contenu du JSON après la conversion
    display_json_content(json_file)

    # Affichage de la confirmation que la conversion est terminée
    print(f"\nData from {csv_file} has been converted to {json_file}")

if __name__ == "__main__":
    main()
