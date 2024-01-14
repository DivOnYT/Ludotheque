import os
from models.classes import Personne
# from models.classes import Ludotheque
from views import menu
from models import base

# Démarrage de l'application
if __name__ == "__main__":
    # Vérification qu'un fichier de sauvegarde existe
    # S'il n'existe pas, on demande les informations concernant la ludotheque
    if not os.path.isfile("sauvegarde.json"):
        print("Premier démarrage : ")
        name = input("Nom de la ludotheque : ") 
        gestionnaire_prenom = input("Prénom du gestionnaire : ")
        gestionnaire_nom = input("Nom du gestionnaire : ")
        gestionnaire_telephone = input("Telephone du gestionnaire : ")
        gestionnaire_adresse = input("Adresse du gestionnaire : ")
        gestionnaire_date_naissance = input("Date de naissance du gestionnaire : ")
        # Création de la ludotheque
        base.create_ludotheque(name, Personne(gestionnaire_prenom, gestionnaire_nom, gestionnaire_telephone, gestionnaire_adresse, gestionnaire_date_naissance))
    else:
        # Comme un fichier de sauvegarde existe, on recharge les données de la ludotheque
        
        # Affichage du menu en passant l'instance de la ludotheque en paramètre
      # Dans main.py
        base.load_ludotheque("sauvegarde.json")
        base.get_ludotheque().repartir()
    menu.menu()


