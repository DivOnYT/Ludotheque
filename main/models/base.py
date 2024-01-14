from models.classes import Ludotheque

# Variable globale
ludotheque: Ludotheque = None

# Récupération de la ludothèque depuis la variable globale
def get_ludotheque():
    global ludotheque
    return ludotheque

# Création de la ludothèque
def create_ludotheque(name, administrator):
    global ludotheque
    if ludotheque is None:
        ludotheque = Ludotheque(name, administrator)

def load_ludotheque(jsonFileName):
    global ludotheque
    if ludotheque is None:
        ludotheque = Ludotheque.load(jsonFileName)
        ludotheque.repartir()

# Création du fichier JSON
def save_ludotheque(jsonFileName):
    global ludotheque
    ludotheque.save(jsonFileName)

