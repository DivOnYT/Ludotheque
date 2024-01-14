from views import personne, emprunt, hobby, game_session
from models import base
from views.hobby import menu_hobbies, Hobby

# Fonction permettant d'effacer les données présentes dans le terminal
def clear_screen():
    print('\x1b[1J')
    return True

# Function permettant de demander des informations à l'utilisateur
def get_input(message='', lowercase=False, default=""):
    input_ = input(message)
    # Si l'input doit être mis en lowercase
    if lowercase:
        input_ = input_.lower()
    # Si l'utilisateur fait juste ENTER, on utilise la valeur par défaut.
    if not input_:
        input_ = default
    return input_


# Définition du menu principal
def menu():
    while True:
        clear_screen()
        # Affichage de l'ASCII art du nom de l'organisation
        print(base.get_ludotheque().nom, "small")
        print()
        command = get_input(
            message='Choose a command [Manage (p)eople / Manage (h)obbies / Manage (e)mprunts / Manage partie(s) / (q)uit]: ',
            lowercase=True
        )

        if command == 'p':
            # Affichage du menu de gestion des personnes
            personne.menu_personnes()
        elif command == 'h':
            # Affichage du menu de gestion des hobbies
            hobby.menu_hobbies(base.get_ludotheque())
        elif command == 'e':
            # Affichage du menu de gestion des emprunts
            emprunt.menu_emprunts() 
        elif command == "s":
            game_session.menu_session()
        elif command == 'q':
            # L'utilisateur a demandé de quitter l'application, nous sauvegardons donc l'ensemble des données.
            base.get_ludotheque().save("sauvegarde.json")
            quit()


