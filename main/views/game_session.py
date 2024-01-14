from datetime import date, timedelta
from models.classes import GameSession, Personne
from models import base
from tabulate import tabulate
from views import menu

"""# Fonction permettant d'effacer les données présentes dans le terminal
def clear_screen():
    print('\x1b[1J')
    return True"""

def ajouter_session_de_jeu():
    print("Veuillez fournir les informations suivantes pour ajouter un partie de jeu avec vos amis :")
    ludotheque = base.get_ludotheque()
    hobb = input("Quel est le nom du hobby avec lequel vous avez joué : ")
    hobby = ludotheque.chercher_hobbies(hobb)
    if hobby == []:
        print("Aucun hobby trouvé.")
        input("Appuyez sur Entrée pour continuer...")
        return
    emprunt = ludotheque.chercher_emprunt_en_cours(hobby)
    if emprunt is None:
        print(f"Le Hobby {hobby.nom} n'est pas emprunté.")
        print("Pour jouer à un hobby vous devez déjà l'emprunter")
        input("Appuyez sur Entrée pour continuer...")
        return
    print(f"Le Hobby {hobby.nom} est emprunté par {emprunt.emprunteur[0].nom}")
    

    print("Entrez les noms des joueurs dans ce pattern : Thomas,Petit,Robert,Richard (les Noms de Famille sont toujours séparés par des virgules)")
    noms = input("Noms : ")
    noms_s = noms.split(",")
    noms_final = []
    for index, nom in enumerate(noms.split(",")):
        joueur = ludotheque.chercher_personne(nom)
        if joueur == None or joueur == "" or joueur == []:
            print(f"Joueur {nom} non trouvée.")
            noms_s.remove(nom)
        else:
            if joueur not in noms_final :
                noms_final.append(joueur)
            if joueur[index].prenom != nom or joueur[index].nom != nom:
                noms_s[index] = joueur[index].prenom
    menu.clear_screen()
    if noms_s == []:
        return
    print(f"La liste finale des personnes ayant participé à ce jeu est : {','.join(noms_s)}")
    print("Entrez les scores dans l'ordre des personnes qui ont participé. Exempe: Thomas,Petit,Robert,Richard\n1,9,5,8 avec 1 pour Thomas et entre virgules\nSi tu rajoutes un 15 à la fin il ne sera pas compté, tous les scores non entrés seront mis à 0")
    scores = input("Scores : ")
    scores_s = scores.split(",")
    if len(noms_s) > len(scores_s):
        while len(noms_s) != len(scores_s):
            scores_s.append("0")
    elif len(noms_s) < len(scores_s):
        while len(noms_s) != len(scores_s):
            scores_s.remove(scores_s[len(scores_s)-1])
    menu.clear_screen()
    print(f"Les Noms finaux sont : {','.join(noms_s)} et les scores finaux sont {','.join(scores_s)}")

    noms_s2 = []
    for x in noms_s:
        noms_s2.append(x.upper())

    run = True
    gagnant_final : Personne
    while run:
        gagnant = input("Quel est le nom du gagnant : ")

        if gagnant.upper() in noms_s2:
            run = False
            gagnant_final = ludotheque.chercher_personne(gagnant)
        else:
            print("Désolé mais le nom du gagnant n'est pas dans la liste de personnes ayant participé au jeu...")

    run = True
    perdant_final : Personne
    while run:
        perdant = input("Quel est le nom du perdant : ")

        if perdant.upper() in noms_s2:
            run = False
            perdant_final = ludotheque.chercher_personne(perdant)
        else:
            print("Désolé mais le nom du perdant n'est pas dans la liste de personnes ayant participé au jeu...")
    menu.clear_screen()
    dater = input("Quelle est la date de ta partie (2023-12-31 -> AAAA-MM-JJ): ")
    try:
        date_s = dater.split('-')
    except:
        return
    print(f"Les Noms sont : {','.join(noms_s)}")
    classement = input("Entrez le classement entre virgules , (1,3,2) correspondant au nom: ")
    classement_s  = classement.split(",")
    comment = input("Des Commentaires sur cette partie (Optional) : ")

    game_s = GameSession(
        _type=None,
        hobby = hobby,
        emprunteur=emprunt.emprunteur[0],
        date_partie=date(int(date_s[0]), int(date_s[1]), int(date_s[2])),
        noms_joueurs=noms_final,
        scores=scores_s,
        classement=classement_s,
        gagnant=gagnant_final,
        perdant=perdant_final,
        commentaires=comment
    )
    ludotheque.ajouter_game_session(game_s)
    base.save_ludotheque("sauvegarde.json")

    print("Session de Jeu ajouté avec succès.")
    input("Appuyez sur entrée pour continuer ...")
    return

def afficher_session_de_jeu():
    ludotheque = base.get_ludotheque()
    game = ludotheque.afficher_game_session()
    print("Liste des Sessions de Jeu :")
    liste = []
    for sessions in game:
        liste.append(sessions.to_string(base.get_ludotheque().gamesession))
    print(tabulate(liste, headers=['#', "Hobby", "Emprunteur", 'Date Partie', 'Noms Joueurs', 'Scores', 'Classement', 'gagnant', 'perdant', 'Commentaire']))
    input("Appuyez sur entrée pour coninuer ...")

def menu_session():
    while True:
        menu.clear_screen()
        print("\nManage parties")
        choix = input("1) Enregistrer une partie de jeu avec vos amis\n2) Consulter les parties enregistrées\n3) Retour\n\nEntrez le numéro de votre choix : ")
        if choix == "1":
            #le menu pour ajouter une session de jeu
            ajouter_session_de_jeu()
        elif choix == "2":
            #afficher les sessions de jeu
            afficher_session_de_jeu()
        elif choix == "3":
            return  # Correction : ajout du return
        else:
            print("Choix invalide.")
