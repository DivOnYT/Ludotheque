from datetime import date
from models.classes import JeuDeSociete
from models import base
from tabulate import tabulate

def ajouter_jeu_de_societe():
    print("Veuillez fournir les informations suivantes pour ajouter un jeu de société :")
    nom = input("Nom : ")
    editeur = input("Éditeur : ")
    distributeur = input("Distributeur : ")
    annee = int(input("Année : "))
    graphisme = input("Graphisme : ")
    illustration = input("Illustration : ")
    mode = input("Mode (coopératif/compétitif) : ")
    nb_joueurs_min = int(input("Nombre de joueurs minimum : "))
    nb_joueurs_max = int(input("Nombre de joueurs maximum : "))
    duree = int(input("Durée d'une partie en minutes : "))
    age_min = int(input("Âge minimum recommandé : "))
    duree_moyenne = int(input("Durée moyenne d'une partie en minutes : "))
    categorie = input("Catégorie : ")
    description = input("Description : ")


    jeu_de_societe = JeuDeSociete(
        nom=nom, 
        editeur=editeur, 
        distributeur=distributeur, 
        annee=annee, 
        graphisme=graphisme, 
        illustration=illustration, 
        mode=mode, 
        nb_joueurs_min=nb_joueurs_min, 
        nb_joueurs_max=nb_joueurs_max, 
        duree=duree, 
        age_min=age_min, 
        duree_moyenne=duree_moyenne,
        categorie=categorie,
        description=description
    )

    ludotheque = base.get_ludotheque()
    ludotheque.ajouter_jeu_de_societe(jeu_de_societe)
    base.save_ludotheque("sauvegarde.json")

    print("Jeu de société ajouté avec succès.")
    input("Appuyez sur entrée pour continuer ...")
    return

def modifier_jeu_de_societe():
    jds = base.get_ludotheque().afficher_jeu_de_societe()
    if not jds:
        print("Il n'y a aucun Jeu de Societe à modifier.")
        return

    nom = input("Entrez le nom du Jeu de Societe à modifier : ")
    jds_a_modifier = base.get_ludotheque().chercher_jeu_de_societe(nom)  # modif by chatgpt
   
    if not jds_a_modifier:
        print(f"Aucun Jeu de Societe nommé {nom} n'a été trouvé.")
        return
    
    description = input(f"Entrez la nouvelle description de {nom} : ")
    categorie = input(f"Entrez la nouvelle catégorie de {nom} : ")
    editeur = input(f"Entrez le nouvel éditeur de {nom} : ")
    distributeur = input(f"Entrez le nouveau distributeur de {nom} : ")
    annee = int(input(f"Entrez la nouvelle année de sortie de {nom} : "))  # modif by chatgpt
    graphisme = input(f"Entrez le nouveau graphisme de {nom} : ")
    illustration = input(f"Entrez la nouvelle illustration de {nom} : ")
    mode = input(f"Entrez le nouveau mode de {nom} (coopératif/compétitif) : ")
    nb_joueurs_min = int(input(f"Entrez le nouveau nb de joueurs Min de {nom} : "))
    nb_joueurs_max = int(input(f"Entrez le nouveau nb de joueurs Max de {nom} : "))
    duree = int(input(f"Entrez la nouvelle durée de {nom} : "))
    age_min = int(input(f"Entrez le nouvel age min de {nom} : "))
    duree_moyenne = int(input(f"Entrez la nouvelle duree moyenne de {nom} : "))

    jds_a_modifier = jds_a_modifier[0]

    jds_a_modifier.description = description
    jds_a_modifier.categorie = categorie
    jds_a_modifier.editeur = editeur
    jds_a_modifier.distributeur = distributeur
    jds_a_modifier.annee = date(annee, 1, 1)
    jds_a_modifier.graphisme = graphisme
    jds_a_modifier.illustration = illustration
    jds_a_modifier.mode = mode
    jds_a_modifier.nb_joueurs_min = nb_joueurs_min
    jds_a_modifier.nb_joueurs_max = nb_joueurs_max
    jds_a_modifier.duree = duree
    jds_a_modifier.age_min = age_min
    jds_a_modifier.duree_moyenne = duree_moyenne

    print(f"Le Jeu de Societe {nom} a été modifié avec succès.")
    input("Appuyez sur entrée pour continuer ...")

def supprimer_jeu_de_societe():
    nom = input("Nom du jeu de société à supprimer : ")
    jeu_de_societe = base.get_ludotheque().chercher_jeu_de_societe(nom)
    if not jeu_de_societe:
        print(f"Aucun jeu de société nommé '{nom}' trouvé.")
        return
    base.get_ludotheque().supprimer_jeu_de_societe(jeu_de_societe)
    base.save_ludotheque("sauvegarde.json")
    print(f"Le jeu de société '{nom}' a été supprimé avec succès.")
    input("Appuyez sur entrée pour continuer ...")


def afficher_jeu_de_societe():
    jeu_de_societe = base.get_ludotheque().afficher_jeu_de_societe()
    if not jeu_de_societe:
        print("Il n'y a aucun jeu de société à afficher.")
        return

    print("Liste des jeux de société:")
    liste = []
    for jeu_de_societe in jeu_de_societe:
        liste.append(jeu_de_societe.to_string(base.get_ludotheque().jeu_de_societe))
    print(tabulate(liste, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Nb Joueur Min', 'Nb Joueur Max', "Duree", "Age Min", "Duree Moyenne", "Description", "Categorie"]))

def chercher_jeu_de_societe():
    nom = input("Nom du jeu de société : ")
    jeu_de_societe = base.get_ludotheque().chercher_jeu_de_societe(nom)
    if not jeu_de_societe:
        print("Aucun jeu de société trouvé.")
        input("Appuyez sur entrée pour continuer ...")
    else:
        print(jeu_de_societe[0].printor())
        input("Appuyez sur Entrée pour continuer...")
        return jeu_de_societe[0]
    return

"""def menu_jeu_de_societe():
    while True:
        print("Menu des jeux de société")
        print("1. Ajouter un jeu de société")
        print("2. Supprimer un jeu de société")
        print("3. Afficher la liste des jeux de société")
        print("4. Chercher un jeu de société")
        print("5. Retour")

        choix = input("Entrez le numéro de votre choix: ")

        if choix == "1":
            ajouter_jeu_de_societe()

        elif choix == "2":
            supprimer_jeu_de_societe()

        elif choix == "3":
            afficher_jeu_de_societe()

        elif choix == "4":
            chercher_jeu_de_societe()

        elif choix == "5":
            print("Retour au menu principal")
            break

        else:
            print("Choix invalide.")
"""