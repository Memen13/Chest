#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, where
from Functions import *
from Models import *
from View import *

class Tournament:
    def __init__(self, id, name, localisation, d_start, d_end, kind, description, round):
        self.id = id
        self.name = name
        self.localisation = localisation
        self.d_start = d_start
        self.d_end = d_end
        self.round = 4
        self.kind = kind
        self.description = description

        print(f'Le tournois {self.name} a été créé')

    def save_tournament(self):
        """ Add le tournois à la bdd qui est déjà créée"""
        serialized_tournament = {
            'Nom': self.name,
            'Localisation': self.localisation,
            'Jour du début': self.d_start,
            'Jour de fin': self.d_end,
            'Round': self.round,
            'Règles': self.kind,
            'Description': self.description}
        db = tinyDB('TournamentDatabase.json')
        table = db.table('Tournois')
        table.insert(serialized_tournament)

def change_tournament_info():
    """

    Fonction qui permet la modification des informations principales d'un tournois déjà existant.
 faire
    """
    while True:
        choice = input("Que voulez vous mettre à jour ? \n 1 : Le nom\n 2 : La localisation\n 3 : La date du début\n"
                       "4 : La date de fin \n 5: Les règles du tournois\n 6 : La description")
        if choice == 1:
            new_name = input("Indiquez le nouveau nom")
            new_tournament.name = new_name
        elif choice == 2:
            new_localisation = input("Indiquez la nouvelle localisation")
            new_tournament.localisation = new_localisation
        elif choice == 3:
            new_tournament.d_start = new_date("de début du tournois, ")
        elif choice == 4:
            new_tournament.d_end = new_date("de fin du tournois,")
        elif choice == 5:
            new_tournament.kind = tournament_rules()
        elif choice == 6:
            new_description = input("Renseignez la nouvelle description du tournois")
            new_tournament.description = new_description
        elif choice == 7:
            print("Très bien, ne changeons rien!")
            break

        other_choice = input("Voulez vous modifier autre chose ? Tapez Oui ou Non")
        if other_choice.lower() == "non":
            break
        elif other_choice.lower() == "oui":
            change_tournament_info()

creation_tournament = input("Voulez vous créer un tournois ? Tapez 1 pour oui ou 2 pour non")
if creation_tournament == "1":
    """Ajout d'une boucle pour verifier les id sur le json tournamentDatabase"""
    id = 1

    name = input("Indiquez le nom du tournois")
    localisation = input("Indiquez la localisation")
    start_day = new_date
    end_day = new_date
    kind = tournament_rules
    description = input("Renseignez la description du tournois")
    round = 4

    choice = input("Souhaitez-vous voir la liste des joueurs inscrits sur le programme? Tapez 1 pour oui, 2 pour non")
    if choice == "1":
        player_json()
    else:
        break



def add_player_to_tournament():
    players_on_tournament = []
    # Entrer la liste des joueurs pour le tournois.
    db = TinyDB('PlayerDatabase.json')
    for i in range(8):
        add_players = input("Indiquez les ID des joueurs à intégrer au tournois")
        # Get data from `player's id`


def search_by_player_name():
    player_seek = input("Indiquez le nom du joueur que vous recherchez")
    player = Query()
    result = db.table('PlayerDatabase.json').search(player.name == player_seek)
    print(result)


listeID = list()
data_player = "PlayerDatabase.json"
for i in data_player.all():
  print(db.get((where('nom') == i["nom"]) and (where("prenom") == i["prenom"])).doc_id)
  listeID.append(db.get((where('nom') == i["nom"]) and (where("prenom") == i["prenom"])).doc_id)

1- Afficher l'ensemble des informations nécessaires pour choisir les joueurs (ID, nom, prénom...)
2- Faire une boucle pour lui donner la possibilité de d'indiquer les ID des joueurs qu'il veut
3- Récupérer les infos des joueurs des ID susmentionné












new_tournament = Tournament(id, name, localisation, d_start, d_end, kind, description, round)
choix = input("Voulez vous modifier quelque chose ? Tapez oui ou non")
if choix.lower() == "oui":
    change_tournament_info(new_tournament)
else:
    print("Ce sera pour une prochaine fois")


