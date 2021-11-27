#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query
import datetime
from View.Recurrent import *
from Controllers.Tournament import *


class Tournament:
    def __init__(self):
        self.name = input("Indiquez le nom du tournois")
        self.localisation = input("Indiquez la localisation du tournois")
        self.day_start = input("") # utiliser datetime
        self.day_end = input("") # fonction pour indiquer si le tournois est terminé. Si oui, utiliser datetime.
        self.kind = tournament_rules()
        self.description = input("Indiquez la description du tournois")
        self.number_of_round = print("Le tournois comporte 4 rounds")
        self.player_on_tournament = add_player_to_tournament()

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

def create_data_tournament():
    db = TinyDB('TournamentDatabase.json')
    table = db.table("Tournois")

def update(self, objectTournament):
    self.table.insert({"name": objectTournament.name})


"""def add_player(self):
    # une boucle qui va ajoute 8 joueurs et sauvegarder à chaque ajout dun joueur
    # Ouvrir le json avec tinydb pour utiliser la méthode .get
    i = 1
    while i < 9:
        player_for_tournament = input("Veuillez indiquer l'id du joueur que vous souhaitez intégrer au tournois")
        player_to_add = db.table("Players").get(doc_id=int(player_for_tournament))
        self.table.insert(player_to_add)
        i = i + 1"""
