from datetime import date
from models.classes import JeuDeRole
from models import base
from tabulate import tabulate


def ajouter_jeu_de_role():
    print("Veuillez fournir les informations suivantes pour ajouter un jeu de rôle :")
    nom = input("Nom : ")
    editeur = input("Éditeur : ")
    distributeur = input("Distributeur : ")
    annee = int(input("Année : "))
    graphisme = input("Graphisme : ")
    illustration = input("Illustration : ")
    mode = bool(int(input("Mode (0 = solo, 1 = multijoueur) : ")))
    systeme_de_jeu = input("Système de jeu : ")
    univers = input("Univers : ")
    description = input("Description : ")
    categorie = input("Catégorie : ")

    jeu_de_role = JeuDeRole(
        nom=nom, 
        editeur=editeur, 
        distributeur=distributeur, 
        annee=date(annee, 1, 1), 
        graphisme=graphisme, 
        illustration=illustration, 
        mode=mode, 
        systeme_de_jeu=systeme_de_jeu, 
        univers=univers,
        description=description,
        categorie=categorie
    )

    ludotheque = base.get_ludotheque()
    ludotheque.ajouter_jeu_de_role(jeu_de_role)
    base.save_ludotheque("sauvegarde.json")

    print("Jeu de rôle ajouté avec succès.")
    input("Appuyez sur entrée pour continuer ...")
    return

def supprimer_jeu_de_role():
    nom = input("Nom du jeu de rôle à supprimer : ")
    ludotheque = base.get_ludotheque()
    jeu_de_role = ludotheque.chercher_jeu_de_role(nom)

    if not jeu_de_role:
        print("Aucun jeu de rôle trouvé.")
    else:
        ludotheque.supprimer_jeu_de_role(jeu_de_role)
        base.save_ludotheque("sauvegarde.json")
        print("Le jeu de rôle a été supprimé avec succès.")
        input("Appuyez sur entrée pour continuer ...")

def modifier_jeu_de_role():
    jdr = base.get_ludotheque().afficher_jeu_de_role()
    if not jdr:
        print("Il n'y a aucun Jeu de Role à modifier.")
        return

    nom = input("Entrez le nom du Jeu de Role à modifier : ")
    jdr_a_modifier = base.get_ludotheque().chercher_jeu_de_role(nom)  # modif by chatgpt
   
    if not jdr_a_modifier:
        print(f"Aucun Jeu de Role nommé {nom} n'a été trouvé.")
        return

    description = input(f"Entrez la nouvelle description de {nom} : ")
    categorie = input(f"Entrez la nouvelle catégorie de {nom} : ")
    editeur = input(f"Entrez le nouvel éditeur de {nom} : ")
    distributeur = input(f"Entrez le nouveau distributeur de {nom} : ")
    annee = int(input(f"Entrez la nouvelle année de sortie de {nom} : "))  # modif by chatgpt
    graphisme = input(f"Entrez le nouveau graphisme de {nom} : ")
    illustration = input(f"Entrez la nouvelle illustration de {nom} : ")
    mode = bool(int(input(f"Entrez le nouveau mode de {nom} (0 = solo, 1 = multijoueur) : ")))
    systeme_de_jeu = input(f"Entrez le nouveau système de jeu de {nom} : ")
    univers = input(f"Entrez le nouvel univers de {nom} : ")

    jdr_a_modifier = jdr_a_modifier[0]

    jdr_a_modifier.description = description
    jdr_a_modifier.categorie = categorie
    jdr_a_modifier.editeur = editeur
    jdr_a_modifier.distributeur = distributeur
    jdr_a_modifier.annee = date(annee, 1, 1)
    jdr_a_modifier.graphisme = graphisme
    jdr_a_modifier.illustration = illustration
    jdr_a_modifier.mode = mode
    jdr_a_modifier.systeme_de_jeu = systeme_de_jeu
    jdr_a_modifier.univers = univers

    print(f"Le Jeu de Role {nom} a été modifié avec succès.")
    input("Appuyez sur entrée pour continuer ...")

def afficher_jeu_de_role():
    jeux_de_role = base.get_ludotheque().afficher_jeu_de_role()
    if not jeux_de_role:
        print("Il n'y a aucun jeu de rôle à afficher.")
        input("Appuyez sur entrée pour continuer ...")
        return

    print("Liste des jeux de rôle :")
    liste = []
    for jeu_de_role in jeux_de_role:
        liste.append(jeu_de_role.to_string(base.get_ludotheque().jeu_de_role))
    print(tabulate(liste, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Genre', 'Plateforme', "Pegi",  "Description", "Categorie"]))

def chercher_jeu_de_role():
    nom = input("Nom du jeu de rôle : ")
    jeu_de_role = base.get_ludotheque().chercher_jeu_de_role(nom)
    if not jeu_de_role:
        print("Aucun jeu de rôle trouvé.")
        input("Appuyez sur entrée pour continuer ...")
    else:
        print(jeu_de_role[0].printor())

        input("Appuyez sur Entrée pour continuer...")
        return jeu_de_role[0]
    return




"""def menu_jeu_de_role():
    while True:
        print("Menu des jeux de rôle")
        print("1. Ajouter un jeu de rôle")
        print("2. Supprimer un jeu de rôle")
        print("3. Afficher la liste des jeux de rôle")
        print("4. Chercher un jeu de rôle")
        print("5. Retour")

        choix = input("Entrez le numéro de votre choix: ")

        if choix == "1":
            ajouter_jeu_de_role()
        elif choix == "2":
            supprimer_jeu_de_role()
        elif choix == "3":
            afficher_jeu_de_role()
        elif choix == "4":
            chercher_jeu_de_role()
        elif choix == "5":
            break
        else:
            print("Choix invalide.")"""