#!/usr/bin/env python3
from task_01_pickle import CustomObject

def main():
    # Créer une instance de CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    
    print("Original Object:")
    obj.display()

    # Sérialiser l'objet dans un fichier
    obj.serialize("object.pkl")

    # Désérialiser l'objet dans une nouvelle instance
    new_obj = CustomObject.deserialize("object.pkl")
    
    print("\nDeserialized Object:")
    new_obj.display()

# Vérifier si le script est exécuté directement
if __name__ == "__main__":
    main()
