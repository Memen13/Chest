#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from Functions import *
from Models import *
import json

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
    def save_tournament():
    """ Add le tournois à la bdd qui est déjà créée"""
        serialized_tournament = {
            'Nom': self.name,
            'Localisation': self.localisation,
            'Jour du début': self.d_start,
            'Jour de fin': self.d_end,
            'Round': self.round,
            'Règles': self.kind,
            'Description': self.description}
        insert(serialized_tournament)

def change_tournament_info():
    """

    Fonction qui permet la modification des informations principales d'un tournois déjà existant.

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
    # Entrer la liste des joueurs pour le tournois.



new_tournament = Tournament(id, name, localisation, d_start, d_end, kind, description, round)
choix = input("Voulez vous modifier quelque chose ? Tapez oui ou non")
if choix.lower() == "oui":
    change_tournament_info(new_tournament)
else:
    print("Ce sera pour une prochaine fois")


