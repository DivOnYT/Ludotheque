from datetime import date
from models.classes import JeuVideo
from models import base
from tabulate import tabulate

def ajouter_jeu_video():
    print("Veuillez fournir les informations suivantes pour ajouter un jeu vidéo :")
    nom = input("Nom : ")
    editeur = input("Éditeur : ")
    distributeur = input("Distributeur : ")
    annee = int(input("Année : "))
    graphisme = input("Graphisme : ")
    illustration = input("Illustration : ")
    mode = bool(int(input("Mode (0 = solo, 1 = multijoueur) : ")))
    genre = input("Genre : ")
    plateforme = input("Plateforme : ")
    pegi = int(input("Pegi : "))
    description = input("Description : ")
    categorie = input("Categorie : ")

    jeu_video = JeuVideo(
        nom=nom, 
        editeur=editeur, 
        distributeur=distributeur, 
        annee=date(annee, 1, 1), 
        graphisme=graphisme, 
        illustration=illustration, 
        mode=mode, 
        genre=genre, 
        plateforme=plateforme, 
        pegi=pegi,
        description=description,
        categorie=categorie
    )

    ludotheque = base.get_ludotheque()
    ludotheque.ajouter_jeu_video(jeu_video)
    base.save_ludotheque("sauvegarde.json")

    print("Jeu vidéo ajouté avec succès.")
    input("Appuyez sur entrée pour continuer ...")
    return

def modifier_jeu_video():
    jvideo = base.get_ludotheque().afficher_jeu_video()
    if not jvideo:
        print("Il n'y a aucun Jeu Video à modifier.")
        return

    nom = input("Entrez le nom du Jeu Video à modifier : ")
    jvideo_a_modifier = base.get_ludotheque().chercher_jeu_video(nom)  # modif by chatgpt
   
    if not jvideo_a_modifier:
        print(f"Aucun Jeu Video nommé {nom} n'a été trouvé.")
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

    jvideo_a_modifier = jvideo_a_modifier[0]

    jvideo_a_modifier.description = description
    jvideo_a_modifier.categorie = categorie
    jvideo_a_modifier.editeur = editeur
    jvideo_a_modifier.distributeur = distributeur
    jvideo_a_modifier.annee = date(annee, 1, 1)
    jvideo_a_modifier.graphisme = graphisme
    jvideo_a_modifier.illustration = illustration
    jvideo_a_modifier.mode = mode
    jvideo_a_modifier.plateforme = plateforme
    jvideo_a_modifier.pegi = pegi
    jvideo_a_modifier.genre = genre

    print(f"Le Jeu Video {nom} a été modifié avec succès.")
    input("Appuyez sur entrée pour continuer ...")

def supprimer_jeu_video():
    nom = input("Nom du jeu vidéo : ")
    ludotheque = base.get_ludotheque()
    jeu_video = ludotheque.chercher_jeu_video(nom)
    if not jeu_video:
        print("Aucun jeu vidéo trouvé.")
        return
    ludotheque.supprimer_jeu_video(jeu_video)
    base.save_ludotheque("sauvegarde.json")
    print("Jeu vidéo supprimé avec succès.")
    input("Appuyez sur entrée pour continuer ...")


def afficher_jeux_video():
    jeux_video = base.get_ludotheque().afficher_jeu_video()
    if not jeux_video:
        print("Il n'y a aucun jeu vidéo à afficher.")
        return

    print("Liste des jeux vidéo:")
    liste = []
    for jeu_video in jeux_video:
        liste.append(jeu_video.to_string(base.get_ludotheque().jeu_video))
    print(tabulate(liste, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Genre', 'Plateforme', "Duree", "Pegi", "Description", "Categorie"]))


def chercher_jeu_video():
    nom = input("Nom du jeu vidéo : ")
    jeu_video = base.get_ludotheque().chercher_jeu_video(nom)
    if not jeu_video:
        print("Aucun jeu vidéo trouvé.")
        input("Appuyez sur entrée pour continuer ...")
    else:
        print(jeu_video[0].printor())

        input("Appuyez sur Entrée pour continuer...")
        return jeu_video[0]
    return

"""def menu_jeu_video():
    while True:
        print("Menu du jeu vidéo")
        print("1. Ajouter un jeu vidéo")
        print("2. Supprimer un jeu vidéo")
        print("3. Afficher les jeux vidéo")
        print("4. Chercher un jeu vidéo")
        print("5. Retour")
        choix = int(input("Choix : "))
        if choix == 1:
            ajouter_jeu_video()
        elif choix == 2:
            supprimer_jeu_video()
        elif choix == 3:
            afficher_jeux_video()
        elif choix == 4:
            chercher_jeu_video()
        elif choix == 5:
            return
        else:
            print("Choix invalide.")"""
