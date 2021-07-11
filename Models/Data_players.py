# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query

def create_data():
    db = TinyDB('PlayerDatabase.json')
    table = db.table("Players")
    global table

def insert(serial):
     table.insert(serial)

def update():
    #Prendre l'id du joueur
    #table.search(where("id") == "METTRE L'ID DU JOUEUR"
    #Créer une nouvelle fonction pour la modification du joueur


# ajouter une condition pour vérifier si la bss existe avant d'instancier
       """ def update(self):
            self.table.insert({"name": self.objectTournament.name})



