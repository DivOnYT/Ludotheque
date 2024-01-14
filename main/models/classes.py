import json
from typing import List
from datetime import date
from tabulate import tabulate

# Sérialisation de nos objets
def custom_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    return {'__class__': obj.__class__.__name__, '__value__': obj.to_dict()}

# Dé-sérialisation des objets JSON.
def custom_deserializer(obj):
    if '__class__' in obj:
        class_name = obj.pop('__class__')
        if class_name == 'Ludotheque':
            return Ludotheque(**obj['__value__'])
        elif class_name == 'Hobby':
            return Hobby(**obj['__value__'])
        elif class_name == 'Personne':
            return Personne(**obj['__value__'])
        elif class_name == 'Emprunt':
            return Emprunt(**obj['__value__'])
        elif class_name == 'JeuDeSociete':
            return JeuDeSociete(**obj['__value__'])
        elif class_name == 'JeuDeRole':
            return JeuDeRole(**obj["__value__"])
        elif class_name == 'JeuVideo':
            return JeuVideo(**obj['__value__'])
        elif class_name == 'GameSession':
           return GameSession(**obj['__value__'])
        else:
            raise TypeError('Unknown class: ' + class_name)
    return obj

class Hobby:
    def __init__(self, nom: str, editeur: str, distributeur: str, annee: date, graphisme: str, illustration: str, mode: bool, genre: str, plateforme: str, pegi: int, description: str, categorie: str):
        self._nom = nom
        self._editeur = editeur
        self._distributeur = distributeur
        self._annee = annee
        self._graphisme = graphisme
        self._illustration = illustration
        self._mode = mode
        self._genre = genre
        self._plateforme = plateforme
        self._pegi = pegi
        self._description = description
        self._categorie = categorie

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def editeur(self):
        return self._editeur

    @editeur.setter
    def editeur(self, value):
        self._editeur = value

    @property
    def distributeur(self):
        return self._distributeur

    @distributeur.setter
    def distributeur(self, value):
        self._distributeur = value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, value):
        self._annee = value

    @property
    def graphisme(self):
        return self._graphisme

    @graphisme.setter
    def graphisme(self, value):
        self._graphisme = value

    @property
    def illustration(self):
        return self._illustration

    @illustration.setter
    def illustration(self, value):
        self._illustration = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def plateforme(self):
        return self._plateforme

    @plateforme.setter
    def plateforme(self, value):
        self._plateforme = value

    @property
    def pegi(self):
        return self._pegi

    @pegi.setter
    def pegi(self, value):
        self._pegi = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def categorie(self):
        return self._categorie

    @categorie.setter
    def categorie(self, value):
        self._categorie = value

    def to_dict(self):
        return {
            'nom': self.nom,
            'editeur': self.editeur,
            'distributeur': self.distributeur,
            'annee': self.annee,
            'graphisme': self.graphisme,
            'illustration': self.illustration,
            'mode': self.mode,
            'genre': self.genre,
            'plateforme': self.plateforme,
            'pegi': self.pegi,
            'description': self.description,
            'categorie': self.categorie
        }
    
    def to_string(self, rows=[]): # fonction added by cmdherouville
        all_secrets = [[index, self.nom, self.editeur, self.distributeur, self.annee, self.graphisme, self.illustration, self.mode, self.genre, self.plateforme, self.pegi, self.description, self.categorie] for index, personne in enumerate(rows)]

        if len(all_secrets) > 0:
            return all_secrets[0]
            #return tabulate(all_secrets, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', "Genre", "Plateforme", "Pegi", "Description", "Categorie"])
        else:
            return 'Aucun Hobby!'
    
    def printor(self):
        printed = f"Nom : {self.nom} - Editeur : {self.editeur} - Distributeur : {self.distributeur} - Annee : {self.annee} - Graphisme : {self.graphisme} - Illustration : {self.illustration} - Mode : {self.mode} - Genre : {self.genre} - Plateforme : {self.plateforme} - Pegi : {self.pegi} - Description : {self.description} - Categorie : {self.categorie}"
        return printed

class Personne:
    def __init__(self, prenom: str, nom: str, telephone: int, adresse: str, date_naissance: date):
        self.__prenom = prenom
        self.__nom = nom
        self.__telephone = telephone
        self.__adresse = adresse
        self.__date_naissance = date_naissance
        

    # Définition des Accesseurs et Mutateurs
    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, new_value):
        self.__prenom = new_value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, new_value):
        self.__nom = new_value

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, new_value):
        self.__telephone = new_value

    @property
    def adresse(self):
        return self.__adresse
    
    @adresse.setter
    def adresse(self, new_value):
        self.__adresse = new_value
    
    @property
    def date_naissance(self):
        return self.__date_naissance
    
    @date_naissance.setter
    def date_naissance(self, new_value):
        self.__date_naissance = new_value
    


    # Nous n'avons pas envie de voir les '__' dans le json généré,
    # nous définition donc la méthode to_dict qui met en forme les données
    # comme nous le souhaitons.
    def to_dict(self):
        return {
        'prenom': self.__prenom,
        'nom': self.__nom,
        'telephone': self.__telephone,
        'adresse': self.__adresse,
        'date_naissance': self.__date_naissance,
        
    }

    

class GameSession():
    def __init__(self, _type, hobby : Hobby, emprunteur : Personne, date_partie: date, noms_joueurs: List[str], scores: List[int], classement: List[int], gagnant: str, perdant: str, commentaires: str):
        super().__init__()
        self.__hobby = hobby
        self.__emprunteur = emprunteur
        self.__date_partie = date_partie
        self.__noms_joueurs = noms_joueurs
        self.__scores = scores
        self.__classement = classement
        self.__gagnant = gagnant
        self.__perdant = perdant
        self.__commentaires = commentaires

    # Accesseurs et mutateurs pour hobby
    @property
    def hobby(self):
        return self.__hobby

    @hobby.setter
    def hobby(self, hobby):
        self.__hobby = hobby

    # Accesseurs et mutateurs pour emprunteur
    @property
    def emprunteur(self):
        return self.__emprunteur

    @emprunteur.setter
    def emprunteur(self, emprunteur):
        self.__emprunteur = emprunteur

    # Accesseurs et mutateurs pour date_partie
    @property
    def date_partie(self):
        return self.__date_partie

    @date_partie.setter
    def date_partie(self, date_partie):
        self.__date_partie = date_partie

    # Accesseurs et mutateurs pour noms_joueurs
    @property
    def noms_joueurs(self):
        return self.__noms_joueurs

    @noms_joueurs.setter
    def noms_joueurs(self, noms_joueurs):
        self.__noms_joueurs = noms_joueurs

    # Accesseurs et mutateurs pour scores
    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, scores):
        self.__scores = scores

    # Accesseurs et mutateurs pour classement
    @property
    def classement(self):
        return self.__classement

    @classement.setter
    def classement(self, classement):
        self.__classement = classement

    # Accesseurs et mutateurs pour gagnant
    @property
    def gagnant(self):
        return self.__gagnant

    @gagnant.setter
    def gagnant(self, gagnant):
        self.__gagnant = gagnant

    # Accesseurs et mutateurs pour perdant
    @property
    def perdant(self):
        return self.__perdant

    @perdant.setter
    def perdant(self, perdant):
        self.__perdant = perdant

    # Accesseurs et mutateurs pour commentaires
    @property
    def commentaires(self):
        return self.__commentaires

    @commentaires.setter
    def commentaires(self, commentaires):
        self.__commentaires = commentaires

    def to_dict(self):
        return {
            '_type': 'GameSession',
            'hobby': self.hobby,
            'emprunteur': self.emprunteur,
            'date_partie': self.date_partie,
            'noms_joueurs': self.noms_joueurs,
            'scores': self.scores,
            'classement': self.classement,
            'gagnant': self.gagnant,
            'perdant': self.perdant,
            'commentaires': self.commentaires
        }

    def to_string(self, rows=[]): # fonction added by cmdherouville
        noms =  []
        for x in self.noms_joueurs:
            noms.append(x[0].nom)
        all_secrets = [[index, self.hobby.nom, self.emprunteur.nom, self.date_partie, ",".join(noms), ",".join(self.scores), ",".join(self.classement), self.gagnant[0].nom, self.perdant[0].nom, self.commentaires] for index, personne in enumerate(rows)]

        if len(all_secrets) > 0:
            return all_secrets[0]
            #return tabulate(all_secrets, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Nb Joueur Min', 'Nb Joueur Max', "Duree", "Age Min", "Duree Moyenne", "Description", "Categorie"])
        else:
            return 'Aucun Jeu De Societe!'


class Emprunt:
    def __init__(self, date_debut: date, date_fin: date, jeu_emprunt: Hobby, emprunteur: Personne, id=None):
        self.id = id 
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__jeu_emprunt = jeu_emprunt
        self.__emprunteur = emprunteur


    # Accesseurs et mutateurs pour date_debut
    @property
    def date_debut(self):
        return self.__date_debut

    @date_debut.setter
    def date_debut(self, date_debut):
        self.__date_debut = date_debut

    # Accesseurs et mutateurs pour date_fin
    @property
    def date_fin(self):
        return self.__date_fin

    @date_fin.setter
    def date_fin(self, date_fin):
        self.__date_fin = date_fin

   # Accesseurs et mutateurs pour jeu_emprunt
    @property
    def jeu_emprunt(self):
        return self.__jeu_emprunt

    @jeu_emprunt.setter
    def jeu_emprunt(self, jeu_emprunt):
        self.__jeu_emprunt = jeu_emprunt

        # Accesseurs et mutateurs pour emprunteur
    @property
    def emprunteur(self):
        return self.__emprunteur

    @emprunteur.setter
    def emprunteur(self, emprunteur):
        self.__emprunteur = emprunteur

        # Accesseurs et mutateurs pour id   

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def to_dict(self):
        try:
            return {
            'id': self.id,
            'jeu_emprunt': self.jeu_emprunt,
            'date_debut': self.date_debut.isoformat(),
            'date_fin': self.date_fin.isoformat(),
            'emprunteur': self.emprunteur
            }
        except:
            return {
            'id': self.id,
            'jeu_emprunt': self.jeu_emprunt,
            'date_debut': self.date_debut,
            'date_fin': self.date_fin,
            'emprunteur': self.emprunteur
        }

    def to_string(self, rows=[]): # fonction added by cmdherouville
        """
        Des try et except, car lorsque qu'il y a 1 emprunt c'est un type Emprunt, si il y en a plus de 2 c'est un type list"""
        try:
            all_secrets = [[index, self.id, self.jeu_emprunt[index].nom, self.date_debut, self.date_fin, self.emprunteur[index].nom, self.jeu_emprunt[index].__class__.__name__] for index, emprunt in enumerate(rows)]
        except:
            try:
                all_secrets = [[index, self.id, self.jeu_emprunt.nom, self.date_debut, self.date_fin, self.emprunteur.nom, self.jeu_emprunt.__class__.__name__] for index, emprunt in enumerate(rows)]
            except:
                all_secrets = [[index, self.id, self.jeu_emprunt.nom, self.date_debut, self.date_fin, self.emprunteur[0].nom, self.jeu_emprunt.__class__.__name__] for index, emprunt in enumerate(rows)]
        if len(all_secrets) > 0:
            return all_secrets[0]
            #return tabulate(all_secrets, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Nb Joueur Min', 'Nb Joueur Max', "Duree", "Age Min", "Duree Moyenne", "Description", "Categorie"])
        else:
            return 'Aucun Emprunt!'
    
class JeuDeSociete(Hobby):
    def __init__(self, nom: str, description: str, categorie: str, editeur: str, distributeur: str, annee: int, graphisme: str, illustration: str, mode: str, nb_joueurs_min: int, nb_joueurs_max: int, duree: int, age_min: int, duree_moyenne: int, _type=None):
        super().__init__(
            nom, editeur, distributeur, annee, graphisme, illustration, mode, "", "", 0, description, categorie
        )
        self._nb_joueurs_min = nb_joueurs_min
        self._nb_joueurs_max = nb_joueurs_max
        self._duree = duree
        self._age_min = age_min
        self._duree_moyenne = duree_moyenne

    @property
    def editeur(self):
        return self._editeur

    @editeur.setter
    def editeur(self, new_value):
        self._editeur = new_value

    @property
    def distributeur(self):
        return self._distributeur

    @distributeur.setter
    def distributeur(self, new_value):
        self._distributeur = new_value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, new_value):
        self._annee = new_value

    @property
    def graphisme(self):
        return self._graphisme

    @graphisme.setter
    def graphisme(self, new_value):
        self._graphisme = new_value

    @property
    def illustration(self):
        return self._illustration

    @illustration.setter
    def illustration(self, new_value):
        self._illustration = new_value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_value):
        self._mode = new_value

    @property
    def nb_joueurs_min(self):
        return self._nb_joueurs_min

    @nb_joueurs_min.setter
    def nb_joueurs_min(self, new_value):
        self._nb_joueurs_min = new_value

    @property
    def nb_joueurs_max(self):
        return self._nb_joueurs_max

    @nb_joueurs_max.setter
    def nb_joueurs_max(self, new_value):
        self._nb_joueurs_max = new_value

    @property
    def duree(self):
        return self._duree

    @duree.setter
    def duree(self, new_value):
        self._duree = new_value

    @property
    def age_min(self):
        return self._age_min

    @age_min.setter
    def age_min(self, new_value):
        self._age_min = new_value

    @property
    def duree_moyenne(self):
        return self._duree_moyenne

    @duree_moyenne.setter
    def duree_moyenne(self, new_value):
        self._duree_moyenne = new_value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, new_value):
        self._description = new_value

    @property
    def categorie(self):
        return self._categorie
    
    @categorie.setter
    def categorie(self, new_value):
        self._categorie = new_value

    def to_dict(self):
        return {
        '_type': 'JeuDeSociete',
        'nom': self._nom,
        'editeur': self._editeur,
        'distributeur': self._distributeur,
        'annee': self._annee,
        'graphisme': self._graphisme,
        'illustration': self._illustration,
        'mode': self._mode,
        'nb_joueurs_min': self._nb_joueurs_min,
        'nb_joueurs_max': self._nb_joueurs_max,
        'duree': self._duree,
        'age_min': self._age_min,
        'duree_moyenne': self._duree_moyenne,
        'description': self._description,
        'categorie': self._categorie
    }

    def to_string(self, rows=[]): # fonction added by cmdherouville
        all_secrets = [[index, self.nom, self.editeur, self.distributeur, self.annee, self.graphisme, self.illustration, self.mode, self._nb_joueurs_min, self._nb_joueurs_max, self.duree, self.age_min, self._duree_moyenne, self._description, self.categorie] for index, personne in enumerate(rows)]

        if len(all_secrets) > 0:
            return all_secrets[0]
            #return tabulate(all_secrets, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Nb Joueur Min', 'Nb Joueur Max', "Duree", "Age Min", "Duree Moyenne", "Description", "Categorie"])
        else:
            return 'Aucun Jeu De Societe!'

    def printor(self):
        printed = f"Nom : {self.nom} - Editeur : {self.editeur} - Distributeur : {self.distributeur} - Annee : {self.annee} - Graphisme : {self.graphisme} - Illustration : {self.illustration} - Nb Joueur Min : {self.nb_joueurs_min} - Nb Joueur Max : {self.nb_joueurs_max} - Duree : {self.duree} - Age Min : {self.age_min} - Duree Moyenne : {self.duree_moyenne} - Description : {self.description} - Categorie : {self.categorie}"
        return printed



class JeuDeRole(Hobby):
    def __init__(self, nom: str, description: str, categorie: str, editeur: str, distributeur: str, annee: date, graphisme: str, illustration: str, mode: bool, systeme_de_jeu: str, univers: str, _type=None):
        super().__init__(
            nom, editeur, distributeur, annee, graphisme, illustration, mode, "", "", 0, description, categorie
        )
        self._editeur = editeur
        self._distributeur = distributeur
        self._annee = annee
        self._graphisme = graphisme
        self._illustration = illustration
        self._mode = mode
        self._systeme_de_jeu = systeme_de_jeu
        self._univers = univers
        self._description = description
        self._categorie = categorie

    @property
    def editeur(self):
        return self._editeur

    @editeur.setter
    def editeur(self, new_value):
        self._editeur = new_value

    @property
    def distributeur(self):
        return self._distributeur

    @distributeur.setter
    def distributeur(self, new_value):
        self._distributeur = new_value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, new_value):
        self._annee = new_value

    @property
    def graphisme(self):
        return self._graphisme

    @graphisme.setter
    def graphisme(self, new_value):
        self._graphisme = new_value

    @property
    def illustration(self):
        return self._illustration

    @illustration.setter
    def illustration(self, new_value):
        self._illustration = new_value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_value):
        self._mode = new_value

    @property
    def systeme_de_jeu(self):
        return self._systeme_de_jeu

    @systeme_de_jeu.setter
    def systeme_de_jeu(self, systeme_de_jeu):
        self._systeme_de_jeu = systeme_de_jeu

    @property
    def univers(self):
        return self._univers

    @univers.setter
    def univers(self, univers):
        self._univers = univers
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def categorie(self):
        return self._categorie
    
    @categorie.setter
    def categorie(self, categorie):
        self._categorie = categorie


    def to_dict(self):
        return {
            '_type': 'JeuDeRole',
            'nom': self._nom,
            'editeur': self._editeur,
            'distributeur': self._distributeur,
            'annee': self._annee,
            'graphisme': self._graphisme,
            'illustration': self._illustration,
            'mode': self._mode,
            'systeme_de_jeu': self._systeme_de_jeu,
            'univers': self._univers,
            'description': self._description,
            'categorie': self._categorie
        }
    
    def to_string(self, rows=[]): # fonction added by cmdherouville
        all_secrets = [[index, self.nom, self.editeur, self.distributeur, self.annee, self.graphisme, self.illustration, self.mode, self.systeme_de_jeu, self.univers, self._description, self.categorie] for index, personne in enumerate(rows)]

        if len(all_secrets) > 0:
            return all_secrets[0]
            #return tabulate(all_secrets, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Genre', 'Plateforme', "Pegi",  "Description", "Categorie"])
        else:
            return 'Aucun Jeu De Role!'

    def printor(self):
        printed = f"Nom : {self.nom} - Editeur : {self.editeur} - Distributeur : {self.distributeur} - Annee : {self.annee} - Graphisme : {self.graphisme} - Illustration : {self.illustration} - Mode : {self.mode} - Système de Jeu : {self.systeme_de_jeu} - Univers : {self.univers} - Description : {self.description} - Categorie : {self.categorie}"
        return printed


class JeuVideo(Hobby):
    def __init__(self, nom: str, description: str, categorie: str, editeur: str, distributeur: str, annee: date, graphisme: str, illustration: str, mode: bool, genre: str, plateforme: str, pegi: int, _type=None):
        super().__init__(
            nom, editeur, distributeur, annee, graphisme, illustration, mode, "", "", 0, description, categorie
        )
        self._editeur = editeur
        self._distributeur = distributeur
        self._annee = annee
        self._graphisme = graphisme
        self._illustration = illustration
        self._mode = mode
        self._genre = genre
        self._plateforme = plateforme
        self._pegi = pegi

    @property
    def editeur(self):
        return self._editeur

    @editeur.setter
    def editeur(self, new_value):
        self._editeur = new_value

    @property
    def distributeur(self):
        return self._distributeur

    @distributeur.setter
    def distributeur(self, new_value):
        self._distributeur = new_value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, new_value):
        self._annee = new_value

    @property
    def graphisme(self):
        return self._graphisme

    @graphisme.setter
    def graphisme(self, new_value):
        self._graphisme = new_value

    @property
    def illustration(self):
        return self._illustration

    @illustration.setter
    def illustration(self, new_value):
        self._illustration = new_value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_value):
        self._mode = new_value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, new_value):
        self._genre = new_value

    @property
    def plateforme(self):
        return self._plateforme

    @plateforme.setter
    def plateforme(self, new_value):
        self._plateforme = new_value

    @property
    def pegi(self):
        return self._pegi

    @pegi.setter
    def pegi(self, new_value):
        self._pegi = new_value

    @property
    def nombre_exemplaires(self):
        return self._nombre_exemplaires

    @nombre_exemplaires.setter
    def nombre_exemplaires(self, new_value):
        self._nombre_exemplaires = new_value

    def to_dict(self):
        return {
            '_type': 'JeuVideo',
            'nom': self._nom,
            'description': self._description,
            'categorie': self._categorie,
            'editeur': self._editeur,
            'distributeur': self._distributeur,
            'annee': self._annee,
            'graphisme': self._graphisme,
            'illustration': self._illustration,
            'mode': self._mode,
            'genre': self._genre,
            'plateforme': self._plateforme,
            'pegi': self._pegi,
        }
    def to_string(self, rows=[]):
        all_secrets = [[index, self.nom, self.editeur, self.distributeur, self.annee, self.graphisme, self.illustration, self.mode, self.genre, self.plateforme, self.pegi, self._description, self.categorie] for index, personne in enumerate(rows)]

        if len(all_secrets) > 0:
            return all_secrets[0]
            #return tabulate(all_secrets, headers=['#', 'Nom', 'Editeur', 'Distributeur', 'Année', 'Graphisme', 'Illustration', 'Mode', 'Genre', 'Plateforme', "Duree", "Pegi", "Description", "Categorie"])
        else:
            return 'Aucun Jeu Vidéo!'
    
    def printor(self):
        printed = f"Nom : {self.nom} - Editeur : {self.editeur} - Distributeur : {self.distributeur} - Annee : {self.annee} - Graphisme : {self.graphisme} - Illustration : {self.illustration} - Mode : {self.mode} - Genre : {self.genre} - Plateforme : {self.plateforme} - Pegi : {self.pegi} - Description : {self.description} - Categorie : {self.categorie}"
        return printed


class Ludotheque:
    def __init__(self, nom, manager, personnes=None, emprunt=None, hobbies=None, gamesession=None):
        self.nom = nom
        self.manager = manager
        self.jeu_de_societe = []
        self.jeu_video = []
        self.jeu_de_role = []
        self.gamesession = gamesession
        self.__personnes = personnes or []
        self.__emprunt = emprunt or []
        self.__hobbies = hobbies or []
    
    def repartir(self): # Permet de faire une update de la ludotheque
        for index, hobbies in enumerate(self.hobbies):
            if isinstance(hobbies, JeuDeRole):
                if hobbies not in self.jeu_de_role:
                    self.jeu_de_role.append(hobbies)
                    self.hobbies.remove(hobbies)
            elif isinstance(hobbies, JeuDeSociete):
                if hobbies not in self.jeu_de_societe:
                    self.jeu_de_societe.append(hobbies)
                    self.hobbies.remove(hobbies)
            elif isinstance(hobbies, JeuVideo):
                if hobbies not in self.jeu_video:
                    self.jeu_video.append(hobbies)
                    self.hobbies.remove(hobbies)
            else:
                pass

        count = 0
        while count != len(self.gamesession) or count < len(self.gamesession):
            game = self.gamesession[count]
            if self.verify_gamesession(game) != True and game in self.gamesession:
                self.gamesession.remove(game)
                print(f"La Session de Jeu liée à l'emprunt du hobby '{game.hobby.nom}' par '{game.emprunteur.nom} {game.emprunteur.prenom}' a été retiré car le hobby ou l'emprunteur ou l'emprunt est introuvables .")
                count = count - 1
                self.save("sauvegarde.json") #ralentit le programme et est sauvegardé après mais faut pas éteindre à ce moment là sinon tout est perdu / Enlever le # pour la sécurité
                input("Appuyez sur entrée pour continuer ...")
            count = count+1

        count = 0
        while count != len(self.emprunt) or count < len(self.emprunt):
            emprunt = self.emprunt[count]
            verify = self.verify_emprunt(emprunt)
            if verify != True and emprunt in self.emprunt:
                self.emprunt.remove(emprunt)
                print(f"L'emprunt du hobby '{emprunt.jeu_emprunt.nom}' par '{emprunt.emprunteur[0].nom} {emprunt.emprunteur[0].prenom}' a été retiré car le hobby ou la personne est introuvable .")
                self.save("sauvegarde.json") #ralentit le programme et est sauvegardé après mais faut pas éteindre à ce moment là sinon tout est perdu / Enlever le # pour la sécurité
                count = count - 1
                input("Appuyez sur entrée pour continuer ...")
            count = count+1

        
    def verify_emprunt(self, emprunt: Emprunt):
        #a = self.chercher_emprunt_en_cours(emprunt.jeu_emprunt, (emprunt.emprunteur[0].nom, emprunt.emprunteur[0].prenom))
        class_name = emprunt.jeu_emprunt.__class__.__name__
        if class_name == "Hobby":
            hobby = self.chercher_hobby(emprunt.jeu_emprunt.nom)

        elif class_name == "JeuDeSociete":
            hobby= self.chercher_jeu_de_societe(emprunt.jeu_emprunt.nom)
    
        elif class_name == "JeuDeRole":
            hobby = self.chercher_jeu_de_role(emprunt.jeu_emprunt.nom)

        elif class_name == "JeuVideo":
            hobby = self.chercher_jeu_video(emprunt.jeu_emprunt.nom)
        
        
        personne = self.chercher_personne(emprunt.emprunteur[0].nom)

        if (hobby == []) or (personne == []):
            return False
        return True

    def verify_gamesession(self, gamesession: GameSession):
        hobby = self.chercher_hobby(gamesession.hobby.nom)
        class_name = gamesession.hobby.__class__.__name__
        if class_name == "Hobby":
            hobby = self.chercher_hobby(gamesession.hobby.nom)

        elif class_name == "JeuDeSociete":
            hobby= self.chercher_jeu_de_societe(gamesession.hobby.nom)
    
        elif class_name == "JeuDeRole":
            hobby = self.chercher_jeu_de_role(gamesession.hobby.nom)

        elif class_name == "JeuVideo":
            hobby = self.chercher_jeu_video(gamesession.hobby.nom)

        emprunteur = self.chercher_personne(gamesession.emprunteur.nom)
        if (hobby == []) or (emprunteur == []):
            return False
        return True
    

    @property
    def personnes(self):
        return self.__personnes
    
    @personnes.setter
    def personnes(self, personnes):
        self.__personnes = personnes
    
    @property
    def emprunt(self):
        return self.__emprunt
    
    @emprunt.setter
    def emprunt(self, emprunt):
        self.__emprunt = emprunt
    
    @property
    def hobbies(self):
        return self.__hobbies
    
    @hobbies.setter
    def hobbies(self, hobbies):
        self.__hobbies = hobbies
    
    def chercher_personne(self, query):
        return [personne for personne in self.personnes
            if query.lower() in personne.prenom.lower()
            or query.lower() in personne.nom.lower()
            or query.lower() in personne.telephone.lower()]
    
    def get_hobby_by_name(self, nom: str):
        for hobby in self.hobbies:
            if hobby.nom== nom:
                return hobby
        return None
    
    def ajouter_hobby(self, hobby):
        self.hobbies.append(hobby)
    
    def modifier_hobby(self, hobby):
        for i in range(len(self.hobbies)):
            if self.hobbies[i].nom == hobby.nom:
                self.hobbies[i] = hobby
                return True
        return False

    def chercher_hobby(self, query):
        return [hobby for hobby in self.hobbies
                if query.lower() in hobby.nom.lower()
                or query.lower() in hobby.description.lower()]

    def chercher_hobbies(self, query):
        for x in [self.hobbies, self.jeu_de_role, self.jeu_video, self.jeu_de_societe]:
            for hobby in x:
                if query.lower() in hobby.nom.lower() or query.lower() in hobby.description.lower():
                    return hobby
            
    
    def supprimer_hobby(self, hobby):
        self.hobbies.remove(hobby)
    
    def afficher_hobbies(self):
        return self.hobbies
    
    def afficher_jeu_de_societe(self):
        return self.jeu_de_societe
    
    def ajouter_jeu_de_societe(self, jeu_de_societe):
        self.jeu_de_societe.append(jeu_de_societe)

    def supprimer_jeu_de_societe(self, jeu_de_societe):
        self.jeu_de_societe.remove(jeu_de_societe[0])
    
    def chercher_jeu_de_societe(self, query):
        return [jeu_de_societe for jeu_de_societe in self.jeu_de_societe
            if query.lower() in jeu_de_societe.nom.lower()
            or query.lower() in jeu_de_societe.description.lower()]

    def ajouter_jeu_video(self, jeu_video):
        self.jeu_video.append(jeu_video)

    def supprimer_jeu_video(self, jeu_video):
        self.jeu_video.remove(jeu_video[0])

    def afficher_jeu_video(self):
        return self.jeu_video
    
    def chercher_jeu_video(self, query):
        return [jeu_video for jeu_video in self.jeu_video
            if query.lower() in jeu_video.nom.lower()
            or query.lower() in jeu_video.description.lower()]
    
    def ajouter_jeu_de_role(self, jeu_de_role):
        self.jeu_de_role.append(jeu_de_role)
    
    def supprimer_jeu_de_role(self, jeu_de_role):
        self.jeu_de_role.remove(jeu_de_role[0])

    def afficher_jeu_de_role(self):
        return self.jeu_de_role
    
    def chercher_jeu_de_role(self, query):
        return [jeu_de_role for jeu_de_role in self.jeu_de_role
            if query.lower() in jeu_de_role.nom.lower()
            or query.lower() in jeu_de_role.description.lower()]

    def supprimer_personne(self, personne):
        self.personnes.remove(personne)

    def ajouter_personne(self, personne):
        self.personnes.append(personne)
    
    def afficher_emprunts(self): # Fonction added by cmdherouville
        return self.emprunt

    def ajouter_emprunt(self, emprunt):
        self.emprunt.append(emprunt)

    def chercher_emprunt_en_cours(self, hobby, nom_prenom=None):
        for emprunt in self.emprunt:
            if emprunt.jeu_emprunt.nom == hobby.nom and str(emprunt.date_fin) >= str(date.today()):
                if hobby and nom_prenom==None:
                    return emprunt
                elif ((nom_prenom[0] == emprunt.emprunteur[0].nom or nom_prenom[1] == emprunt.emprunteur[0].prenom) or (nom_prenom[0] == emprunt.emprunteur[0].prenom or nom_prenom[1] == emprunt.emprunteur[0].nom)) and nom_prenom!=None:#nom_prenom[0] -> Nom / nom_prenom[1] -> Prenom
                    return emprunt

        return None

    def retirer_emprunt(self, emprunt):
        self.emprunt.remove(emprunt)
    
    def ajouter_game_session(self, gamesession):
        self.gamesession.append(gamesession)
    
    def afficher_game_session(self):
        return self.gamesession
    
    def save(self, file_name):
        with open(file_name, 'w') as file:
            file.write(self.toJSON())

    @staticmethod
    def load(file_name):
        with open(file_name) as file:
            return json.loads(file.read(), object_hook=custom_deserializer)  

    def to_dict(self):  
        self.repartir()
        return {
            'nom': self.nom,
            'manager': self.manager,
            'personnes': self.personnes,
            'emprunt': self.emprunt,
            'hobbies': self.hobbies+self.jeu_de_role+self.jeu_de_societe+self.jeu_video,
            'gamesession': self.gamesession
            }
    
    def toJSON(self):
        return json.dumps(self, indent=3, default=custom_serializer)
