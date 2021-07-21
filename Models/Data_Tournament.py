#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query


def create_data_tournament():
    db = TinyDB('TournamentDatabase.json')
    table = db.table("Tournois")
    global table


def insert_tournament(serial):
    table.insert(serial)


def update(self, objectTournament):
    self.table.insert({"name": objectTournament.name})


def add_player(self):
    # une boucle qui va ajoute 8 joueurs et sauvegarder à chaque ajout dun joueur
    # Ouvrir le json avec tinydb pour utiliser la méthode .get
    i = 1
    while i < 9:
        player_for_tournament = input("Veuillez indiquer l'id du joueur que vous souhaitez intégrer au tournois")
        player_to_add = db.table("Players").get(doc_id=int(player_for_tournament))
        self.table.insert(player_to_add)
        i = i + 1
