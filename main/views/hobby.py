from datetime import date
from typing import List
from models.classes import Hobby
from models import base
from .jeu_video import *
from .jeu_de_role import *
from .jeu_de_societe import *
from views import menu
from tabulate import tabulate

# from models.classes import Ludotheque


def ajouter_hobby(ludotheque):
    nom = input("Entrez le nom du hobby : ")
    description = input("Entrez une description du hobby : ")
    categorie = input("Entrez la catégorie du hobby : ")
    editeur = input("Entrez l'éditeur du hobby : ")
    distributeur = input("Entrez le distributeur du hobby : ")

    while True:
        try:
            annee = int(input("Entrez l'année de sortie du hobby : "))
            if annee < 1900 or annee > date.today().year:
                raise ValueError("L'année doit être comprise entre 1900 et l'année en cours.")
            break
        except ValueError:
            print("Erreur : veuillez entrer une année valide.")

    graphisme = input("Entrez le graphisme du hobby : ")
    illustration = input("Entrez l'illustration du hobby : ")
    mode = bool(int(input("Entrez le mode du hobby (0 = solo, 1 = multijoueur) : ")))
    plateforme = input("Entrez la plateforme du hobby : ")
    pegi = input("Entrez le PEGI du hobby : ")
    genre = input("Entrez le genre du hobby : ")

    hobby = Hobby(nom=nom, description=description, categorie=categorie, editeur=editeur, distributeur=distributeur, annee=date(annee, 1, 1), graphisme=graphisme, illustration=illustration, mode=mode, plateforme=plateforme, pegi=pegi, genre=genre)
    ludotheque.ajouter_hobby(hobby)

    print(f"Le hobby {nom} a été ajouté avec succès.")
    input("Apuuyez sur entrée pour continuer ...")


def modifier_hobby(ludotheque):
    hobbies = base.get_ludotheque().afficher_hobbies()
    if not hobbies:
        print("Il n'y a aucun hobby à modifier.")
        return

    nom = input("Entrez le nom du hobby à modifier : ")
    hobby_a_modifier = base.get_ludotheque().get_hobby_by_name(nom)  # modif by chatgpt
   
    if not hobby_a_modifier:
        print(f"Aucun hobby nommé {nom} n'a été trouvé.")
        return

    description = input(f"Entrez la nouvelle description de {nom} : ")
    categorie = input(f"Entrez la nouvelle catégorie de {nom} : ")
    editeur = input(f"Entrez le nouvel éditeur de {nom} : ")
    distributeur = input(f"Entrez le nouveau distributeur de {nom} : ")
    annee = int(input(f"Entrez la nouvelle année de sortie de {nom} : "))  # modif by chatgpt
    graphisme = input(f"Entrez le nouveau graphisme de {nom} : ")
    illustration = input(f"Entrez la nouvelle illustration de {nom} : ")
    mode = bool(int(input(f"Entrez le nouveau mode de {nom} (0 = solo, 1 = multijoueur) : ")))
    plateforme = input(f"Entrez la nouvelle plateforme de {nom} : ")
    pegi = input(f"Entrez le nouveau PEGI de {nom} : ")
    genre = input(f"Entrez le nouveau genre de {nom} : ")

    hobby_a_modifier.description = description
    hobby_a_modifier.categorie = categorie
    hobby_a_modifier.editeur = editeur
    hobby_a_modifier.distributeur = distributeur
    hobby_a_modifier.annee = date(annee, 1, 1)
    hobby_a_modifier.graphisme = graphisme
    hobby_a_modifier.illustration = illustration
    hobby_a_modifier.mode = mode
    hobby_a_modifier.plateforme = plateforme
    hobby_a_modifier.pegi = pegi
    hobby_a_modifier.genre = genre

    print(f"Le hobby {nom} a été modifié avec succès.")
    input("Appuyez sur entrée pour continuer ...")



def supprimer_hobby(ludotheque):
    hobbies = base.get_ludotheque().afficher_hobbies()
    if not hobbies:
        print("Il n'y a aucun hobby à supprimer.")
        return

    nom = input("Entrez le nom du hobby à supprimer : ")

    for hobby in hobbies:
        if hobby.nom == nom:
            base.get_ludotheque().supprimer_hobby(hobby)
            print(f"Le hobby {nom} a été supprimé avec succès.")
            input("Appuyez sur entrée pour continuer ...")
            return

    print(f"Aucun hobby nommé {nom} n'a été trouvé.")


def afficher_hobbies(ludotheque):
    hobbies = base.get_ludotheque().afficher_hobbies()
    if not hobbies:
        print("Il n'y a aucun hobby à afficher.")
        return

    print("Liste des hobbies :")
    liste = []
    for hobby in hobbies:
        liste.append(hobby.to_string(ludotheque.hobbies))
    print(tabulate(liste, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Genre', 'Plateforme', "Pegi", "Description", "Categorie"]))



def chercher_hobby(ludotheque=None):
    query = input("Entrez le nom ou la description du hobby à chercher : ")
    hobbies = base.get_ludotheque().chercher_hobby(query)

    if not hobbies:
        print("Il n'y a aucun hobby à chercher.")
        input("Appuyez sur entrée pour continuer ...")
        return None

    for hobby in hobbies:
        if hobby.nom == query:
            print(f"Le hobby {query} existe.")
            print(hobby.printor())
        input("Appuyez sur entrer pour continuer ...")
        return hobby

    print(f"Aucun hobby nommé {query} n'a été trouvé.")
    input("Appuyez sur entrer pour continuer ...")
    return None



def menu_hobbies(ludotheque):
    while True:
        menu.clear_screen()
        print("Menu des hobbies")
        print("1) Ajouter un Hobby")
        print("2) Modifier un hobby")
        print("3) Supprimer un hobby")
        print("4) Afficher la liste des Hobbys")
        print("5) Chercher un Hobby")
        print("6) Retour")

        choix = input("Entrez le numéro de votre choix : ")

        if choix == "1":
            #ajouter_hobby(ludotheque)
            run = True
            while run:
                menu.clear_screen()
                print("Ajouter un hobby")
                print("1) Hobby Générique")
                print("2) Jeu de Société")
                print("3) Jeu Vidéo")
                print("4) Jeu de Rôle")
                print("5) Retour")
                choix = input("Entrez le numéro de votre choix : ")
                if choix == "1":
                    ajouter_hobby(ludotheque)
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "2":
                    ajouter_jeu_de_societe()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "3":
                    ajouter_jeu_video()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "4":
                    ajouter_jeu_de_role()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "5":
                    run = False


        elif choix == "2":
            #modifier_hobby(ludotheque)
            run = True
            while run:
                menu.clear_screen()
                print("Modifier un Hobby")
                print("1) Modifier un Hobby Générique")
                print("2) Modifier un Jeu de Société")
                print("3) Modifier un Jeu Vidéo")
                print("4) Modifier un Jeu de Rôle")
                print("5) Retour")
                choix = input("Entrez le numéro de votre choix : ")
                if choix == "1":
                    modifier_hobby(ludotheque)
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "2":
                    modifier_jeu_de_societe()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "3":
                    modifier_jeu_video()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "4":
                    modifier_jeu_de_role()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "5":
                    run = False

        elif choix == "3":
            #supprimer_hobby(ludotheque)
            run = True
            while run:
                menu.clear_screen()
                print("Supprimer un Hobby")
                print("1) Supprimer un Hobby Générique")
                print("2) Supprimer un Jeu de Société")
                print("3) Supprimer un Jeu Vidéo")
                print("4) Supprimer un Jeu de Rôle")
                print("5) Retour")
                choix = input("Entrez le numéro de votre choix : ")
                if choix == "1":
                    supprimer_hobby(ludotheque)
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "2":
                    supprimer_jeu_de_societe()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "3":
                    supprimer_jeu_video()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "4":
                    supprimer_jeu_de_role()
                    base.get_ludotheque().save("sauvegarde.json")
                elif choix == "5":
                    run = False
            base.get_ludotheque().save("sauvegarde.json")

        elif choix == "4":
            #afficher_hobbies(ludotheque)
            run = True
            while run:
                menu.clear_screen()
                print("Afficher la liste des Hobby")
                print("1) Afficher tous les hobbies")
                print("2) Afficher tous les jeu de Société")
                print("3) Afficher tous les Jeux Vidéo")
                print("4) Afficher tous les Jeux de Rôle")
                print("5) Retour")
                choix = input("Entrez le numéro de votre choix : ")
                if choix == "1":
                    afficher_hobbies(ludotheque)
                elif choix == "2":
                    afficher_jeu_de_societe()
                elif choix == "3":
                    afficher_jeux_video()
                elif choix == "4":
                    afficher_jeu_de_role()
                elif choix == "5":
                    run = False
                input("Appuyez sur entrée pour continuer")
            base.get_ludotheque().save("sauvegarde.json")
                
                

        elif choix == "5":
            #chercher_hobby(ludotheque)
            run = True
            while run:
                menu.clear_screen()
                print("Chercher un Hobby")
                print("1) Rechercher un Hobby Générique")
                print("2) Rechercher un Jeu de Société")
                print("3) Rechercher un Jeu Vidéo")
                print("4) Rechercher un Jeu de Rôle")
                print("5) Retour")
                choix = input("Entrez le numéro de votre choix : ")
                if choix == "1":
                    chercher_hobby(ludotheque)
                elif choix == "2":
                    chercher_jeu_de_societe()
                elif choix == "3":
                    chercher_jeu_video()
                elif choix == "4":
                    chercher_jeu_de_role()
                elif choix == "5":
                    run = False
            base.get_ludotheque().save("sauvegarde.json")

        elif choix == "6":
            print("Retour au menu principal")
            break

        """elif choix == "6":
            menu_jeu_de_role()

        elif choix == "7":
            menu_jeu_de_societe()

        elif choix == "8":
            menu_jeu_video()"""



