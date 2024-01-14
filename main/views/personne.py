import time

from models.classes import Personne
from . import menu
from tabulate import tabulate
from models import base
from views import menu
# from models.base import gestionnaire

# Fonction générique qui permet d'afficher les informations d'une personne ou plusieurs.
def to_table(rows=[]):
    all_secrets = [[index, personne.prenom, personne.nom, personne.telephone, personne.adresse, personne.date_naissance] for index, personne in enumerate(rows)]

    if len(all_secrets) > 0:
        return tabulate(all_secrets, headers=['#', 'Prénom', 'Nom', 'Numéro de téléphone', 'Adresse', 'Date de naissance'])
    else:
        return 'Aucune personne!'
    
def menu_personnes(next_command=None):
    menu.clear_screen()
    print("Gestion des personnes.")
    if next_command:
        command = next_command
        next_command = None
    else:
        print()
        command = menu.get_input(
            message='Choisissez une commande [(l)ister / (a)jouter / (s)upprimer / (r)echercher / (b)ack]: ',
            lowercase=True
        )
    if command is False:
        print()

    if command == 'l':
        afficher_personnes()
    elif command == 'a':
        ajouter_personne()
    elif command == 'm':
        modifier_personne()
    elif command == 's':
        supprimer_personne()
    elif command == 'r':
        chercher_personne()
    elif command == 'b':
        return False
    menu_personnes(next_command)


def ajouter_personne():
    menu.clear_screen()
    print("Ajouter une personne")
    prenom = menu.get_input(message='* Entrez le prénom de la personne: ')
    if prenom is False:
        return False
    nom = menu.get_input(message='* Entrez le nom de la personne: ')
    if nom is False:
        return False
    telephone = menu.get_input(message='* Entrez le numéro de téléphone de la personne: ')
    if telephone is False:
        return False
    adresse = menu.get_input(message='* Entrez l\'adresse de la personne: ')
    if adresse is False:
        return False
    date_naissance = menu.get_input(message='* Entrez la date de naissance de la personne: ')
    if date_naissance is False:
        return False
    base.save_ludotheque("sauvegarde.json")

    base.get_ludotheque().ajouter_personne(Personne(prenom, nom, telephone, adresse, date_naissance))
    print(f"La personne {prenom} {nom} a été ajoutée avec succès.")
    input("Appuyez sur entrée pour continuer ...")


def modifier_personne(personne):
    menu.clear_screen()
    print("Modification de personne:")
    print(f'* Current firstname {personne.prenom}')
    prenom = menu.get_input('* New firstname: ', default=personne.prenom)
    personne.prenom = prenom
    print(f'* Current lastname {personne.nom}')
    nom = menu.get_input('* New lastname: ', default=personne.nom)
    personne.nom = nom
    print(f'* Current phone number {personne.telephone}')
    telephone = menu.get_input('* New phone number: ', default=personne.telephone)
    personne.telephone = telephone
    base.save_ludotheque("sauvegarde.json")
    print(f"La personne {personne.prenom} {personne.nom} a bien été modifiée ...")
    input("Appuyez sur entrée pour continuer ...")
    return "l"

def supprimer_personne():
    menu.clear_screen()
    print("Supprimer une personne:")
    query = menu.get_input('* Saisir la recherche pour trouver la personne à supprimer: ')
    print('Résultat de la recherche:')
    
    # Remplacer la ligne ci-dessous par la méthode de recherche appropriée pour la classe Personne
    result = base.get_ludotheque().chercher_personne(query)
    
    print(to_table(result))
    print("\n'#' signifie le nombre de la personne dans la liste. Exemple : 1\n")
    id_ = menu.get_input(message='Choisissez une commande [delete (#), (b)ack]: ', lowercase=True)
    
    try:
        id_ = int(id_)
    except ValueError:
        id_ = 'b'

    if id_ != 'b' and id_ + 1 == len(result):
        personne = result[id_]
        base.get_ludotheque().supprimer_personne(personne)
        base.save_ludotheque("sauvegarde.json")
        print(f"La personne {personne.prenom} {personne.nom} a été supprimée avec succès.")
        input("Appuyez sur entrée pour continuer ...")
        return
    return False

# def afficher_personnes():
#     menu.clear_screen()
#     print("Liste des personnes:")
#     personnes = base.get_ludotheque().personnes
#     if not personnes:
#         print("Il n'y a aucune personne à afficher.")
#         return

#     print(to_table([(i, p) for i, p in enumerate(personnes)]))
#     id_ = menu.get_input(message='Choisissez une commande [edit (#), (b)ack]: ', lowercase=True)

#     try:
#         id_ = int(id_)
#     except ValueError:
#         id_ = 'b'

#     if id_ != 'b' and id_ + 1 == len(personnes):
#         return modifier_personne(personnes[id_])
#     return False

def afficher_personnes():
    menu.clear_screen()
    print("Personnes list")
    print(to_table(base.get_ludotheque().personnes))
    print("\n'#' signifie le nombre de la personne dans la liste. Exemple : 1\n")
    id_ = menu.get_input(message='Choose a command [edit (#) , (b)ack]: ', lowercase=True)
    try:
        id_ = int(id_)
    except ValueError:
        id_ = 'b'

    if id_ != 'b' and id_ + 1 == len(base.get_ludotheque().personnes):
        return modifier_personne(base.get_ludotheque().personnes[id_])
    return False

def chercher_personne():
    menu.clear_screen()
    print("Recherche de personne:")
    query = menu.get_input('* Saisir la recherche: ')
    print('Résultat de la recherche:')
    
    # Utiliser la méthode de recherche générique pour la classe Personne
    result = base.get_ludotheque().chercher_personne(query)
    
    print(to_table(result))
    print("\n'#' signifie le nombre de la personne dans la liste. Exemple : 1\n")
    id_ = menu.get_input(message='Choisissez une commande [edit (#), (b)ack]: ', lowercase=True)
    
    try:
        id_ = int(id_)
    except ValueError:
        id_ = 'b'

    if id_ != 'b' and id_ + 1 == len(result):
        # Appeler la méthode d'édition pour effectuer la modification
        return modifier_personne(result[id_])
    return False



