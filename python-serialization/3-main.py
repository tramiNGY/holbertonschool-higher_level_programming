#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    # Exemple de dictionnaire à sérialiser en XML
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    # Nom du fichier XML où les données seront sauvegardées
    xml_file = "data.xml"

    # Sérialisation du dictionnaire en XML
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    # Désérialisation du fichier XML pour obtenir les données sous forme de dictionnaire
    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
