#!/usr/bin/python3
'''
This module takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
'''
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Requête sécurisée avec des paramètres pour éviter l'injection SQL
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))

    # Récupération des résultats
    states = cursor.fetchall()

    # Affichage des résultats
    for state in states:
        print(state)

    # Fermeture de la connexion
    cursor.close()
    db.close()
