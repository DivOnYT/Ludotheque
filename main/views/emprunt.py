from datetime import date, timedelta
from models.classes import Emprunt
from models import base
from views import menu
from views.hobby import chercher_hobby
from views.jeu_de_role import chercher_jeu_de_role
from views.jeu_de_societe import chercher_jeu_de_societe
from views.jeu_video import chercher_jeu_video
from tabulate import tabulate

def emprunter_hobby():
    print("Veuillez fournir les informations suivantes pour emprunter un hobby :")
    ludotheque = base.get_ludotheque()
    hobby = chercher_hobby()
    if hobby is None:
        print("Aucun hobby trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(hobby)
    if emprunt is not None:
        print(f"Le Hobby {hobby.nom} est déjà emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return
    print(f"Hobby sélectionné : {hobby.nom}")
    date_emprunt = date.today()
    date_retour = date_emprunt + timedelta(days=14)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = Emprunt(date_emprunt, date_retour, hobby, emprunteur)
    ludotheque.ajouter_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")
    print("Hobby emprunté avec succès.")
    input("Appuyez sur Entrée pour continuer...")



def rendre_hobby():
    print("Veuillez fournir les informations suivantes pour rendre un hobby :")
    nom = input("Nom du hobby : ")
    ludotheque = base.get_ludotheque()
    hobby = chercher_hobby(nom)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
       
    if hobby is None:
        print("Aucun hobby trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return

    emprunt = ludotheque.chercher_emprunt_en_cours(hobby, [emprunteur_nom, emprunteur_prenom])
    if emprunt is None:
        print(f"Le hobby {hobby.nom} n'est pas emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return

    date_retour = date.fromisoformat(input("Date de retour (format : AAAA-MM-JJ) : "))
    emprunt.date_fin = date_retour

    ludotheque.retirer_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")

    print("Emprunt retiré avec succès.")
    input("Appuyez sur Entrée pour continuer...")
    return

def afficher_emprunts_en_cours():
    ludotheque = base.get_ludotheque()
    emprunts = ludotheque.afficher_emprunts()
    liste = []
    for emprunt in emprunts:
        liste.append(emprunt.to_string(base.get_ludotheque().emprunt))
    print(tabulate(liste, headers=['#', 'ID', 'Hobby Emprunté', 'Date Début', 'Date Fin', 'Emprunteur', 'Type']))
    input("Apuuyez sur entrée pour continuer")

#Jeu de societe emprunter et rendre similaire au emprunter et rendre hobby

def rendre_jeu_de_societe():
    print("Veuillez fournir les informations suivantes pour rendre un Jeu de Societe :")
    nom = input("Nom du Jeu de societe : ")
    ludotheque = base.get_ludotheque()
    jds = ludotheque.chercher_jeu_de_societe(nom)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    if jds is None:
        print("Aucun Jeu de Societe trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(jds[0], [emprunteur_nom, emprunteur_prenom])
    if emprunt is None:
        print(f"Le Jeu de societe {jds[0].nom} n'est pas emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return

    date_retour = date.fromisoformat(input("Date de retour (format : AAAA-MM-JJ) : "))
    emprunt.date_fin = date_retour

    ludotheque.retirer_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")

    print("Emprunt de Jeu de societe retiré avec succès.")
    input("Appuyez sur Entrée pour continuer...")
    return

def emprunter_jeu_de_societe():
    print("Veuillez fournir les informations suivantes pour emprunter un jeu de societe :")
    ludotheque = base.get_ludotheque()
    jds = chercher_jeu_de_societe()
    if jds is None:
        print("Aucun Jeu de Societe trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(jds)
    if emprunt is not None:
        print(f"Le Jeu de Societe {jds.nom} est déjà emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return
    print(f"Jeu de Société sélectionné : {jds.nom}")
    date_emprunt = date.today()
    date_retour = date_emprunt + timedelta(days=14)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = Emprunt(date_emprunt, date_retour, jds, emprunteur)
    ludotheque.ajouter_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")
    print("Jeu de Societe emprunté avec succès.")
    input("Appuyez sur Entrée pour continuer...")

#Jeu Vidéo emprunter et rendre similaire au emprunter et rendre hobby

def rendre_jeu_video():
    print("Veuillez fournir les informations suivantes pour rendre un Jeu Video :")
    nom = input("Nom du Jeu Video : ")
    ludotheque = base.get_ludotheque()
    video = ludotheque.chercher_jeu_video(nom)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    if video is None:
        print("Aucun Jeu Video trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(video[0], [emprunteur_nom, emprunteur_prenom])
    if emprunt is None:
        print(f"Le Jeu Video {video[0].nom} n'est pas emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return

    date_retour = date.fromisoformat(input("Date de retour (format : AAAA-MM-JJ) : "))
    emprunt.date_fin = date_retour

    ludotheque.retirer_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")

    print("Emprunt de Jeu Video retiré avec succès.")
    input("Appuyez sur Entrée pour continuer...")
    return

def emprunter_jeu_video():
    print("Veuillez fournir les informations suivantes pour emprunter un jeu video :")
    ludotheque = base.get_ludotheque()
    video = chercher_jeu_video()
    if video is None:
        print("Aucun Jeu Video trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(video)
    if emprunt is not None:
        print(f"Le Jeu Vidéo {video.nom} est déjà emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return
    print(f"Jeu Video sélectionné : {video.nom}")
    date_emprunt = date.today()
    date_retour = date_emprunt + timedelta(days=14)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = Emprunt(date_emprunt, date_retour, video, emprunteur)
    ludotheque.ajouter_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")
    print("Jeu Video emprunté avec succès.")
    input("Appuyez sur Entrée pour continuer...")

#Jeu de role emprunter et rendre similaire au emprunter et rendre hobby

def rendre_jeu_de_role():
    print("Veuillez fournir les informations suivantes pour rendre un Jeu de Role :")
    nom = input("Nom du Jeu de Role : ")
    ludotheque = base.get_ludotheque()
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    jdr = ludotheque.chercher_jeu_de_role(nom)
    if jdr is None:
        print("Aucun Jeu de Role trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(jdr[0], [emprunteur_nom, emprunteur_prenom])
    if emprunt is None:
        print(f"Le Jeu de Role {jdr[0].nom} n'est pas emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return

    date_retour = date.fromisoformat(input("Date de retour (format : AAAA-MM-JJ) : "))
    emprunt.date_fin = date_retour

    ludotheque.retirer_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")

    print("Emprunt de Jeu de role retiré avec succès.")
    input("Appuyez sur Entrée pour continuer...")
    return

def emprunter_jeu_de_role():
    print("Veuillez fournir les informations suivantes pour emprunter un jeu de role :")
    ludotheque = base.get_ludotheque()
    jdr = chercher_jeu_de_role()
    if jdr is None:
        print("Aucun Jeu de Role trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(jdr)
    if emprunt is not None:
        print(f"Le Jeu de Role {jdr.nom} est déjà emprunté.")
        input("Appuyez sur Entrée pour continuer...")
        return
    print(f"Jeu de Role sélectionné : {jdr.nom}")
    date_emprunt = date.today()
    date_retour = date_emprunt + timedelta(days=14)
    emprunteur_nom = input("Nom de l'emprunteur : ")
    emprunteur_prenom = input("Prénom de l'emprunteur : ")
    emprunteur = ludotheque.chercher_personne(emprunteur_nom)
    if emprunteur is None:
        print("Personne non trouvée.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = Emprunt(date_emprunt, date_retour, jdr, emprunteur)
    ludotheque.ajouter_emprunt(emprunt)
    base.save_ludotheque("sauvegarde.json")
    print("Jeu de Role emprunté avec succès.")
    input("Appuyez sur Entrée pour continuer...")

def menu_emprunts():
    while True:
        menu.clear_screen()
        print("\nGestion des emprunts")
        choix = input("1) Emprunter un hobby\n2) Rendre un hobby\n3) Afficher les emprunts en cours\n4) Retour au menu principal\nEntrez le numéro de votre choix : ")
        if choix == "1":
            #le menu pour emprunter
            run = True
            while run:
                menu.clear_screen()
                choix = input("Emprunter Un Hobby \n1)Emprunter un Hobby Generique\n2)Emprunter un Jeu de Societe\n3)Emprunter un Jeu Vidéo\n4)Emprunter un Jeu de Role\n5)Retour\n>>> ")
                if choix == "1":
                    emprunter_hobby()
                elif choix == "2":
                    emprunter_jeu_de_societe()
                elif choix == "3":
                    emprunter_jeu_video()
                elif choix == "4":
                    emprunter_jeu_de_role()
                elif choix == "5":
                    run = False
                else:
                    print(f"Entrée Invalide. {choix} invalide")
        elif choix == "2":
            run = True
            while run:
                #Le menu pour rendre le hobby etc...
                menu.clear_screen()
                choix = input("Rendre Un Hobby \n1)Rendre un Hobby Generique\n2)Rendre un Jeu de Societe\n3)Rendre un Jeu Vidéo\n4)Rendre un Jeu de Role\n5)Retour\n>>> ")
                if choix == "1":
                    rendre_hobby()
                elif choix == "2":
                    rendre_jeu_de_societe()
                elif choix == "3":
                    rendre_jeu_video()
                elif choix == "4":
                    rendre_jeu_de_role()
                elif choix == "5":
                    run = False
                else:
                    print(f"Entrée Invalide. {choix} invalide")
        elif choix == "3":
            afficher_emprunts_en_cours()
        elif choix == "4":
            return  # Correction : ajout du return
        else:
            print("Choix invalide.")
