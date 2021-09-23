# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query

def create_data_player():
    db = TinyDB('PlayerDatabase.json')
    table = db.table("Players")

def insert_players(serial):
    db = TinyDB('PlayerDatabase.json')
    table = db.table('Players')
    table.insert(serial)


def update():
    #Prendre l'id du joueur
    #table.search(where("id") == "METTRE L'ID DU JOUEUR"
    #Créer une nouvelle fonction pour la modification du joueur



