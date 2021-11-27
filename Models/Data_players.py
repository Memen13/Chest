# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import tinyDB

class Players:
    """
        docstring
    """

    def __init__(self):
        while True:
            self.first_name = input("Prénom du joueur: ")
            self.last_name = input("Nom du joueur: ")
            self.age = int(input("Âge du joueur: "))
            while True:
                self.gender = input("Sexe du joueur: 1: M 2: F")
                if self.gender == "1":
                    self.gender = "Masculin"
                    break
                elif self.gender == "2":
                    self.gender = "Feminin"
                    break
            self.rank = float(input("Elo du joueur: "))

            print(f""" Voici les informations du joueur:
            -Prénom: {self.first_name}
            -Nom: {self.last_name}
            -Âge: {self.age}
            -Sexe: {self.gender}
            -Elo du joueur: {self.rank}
            Souhaitez-vous recommencer la création du joueur afin de modifier une information?""")
            choice = input("Tapez 1 pour oui ou 2 pour non")
            if choice == "1":
                pass

    def save_player(self):
        """ Add le joueur à la bdd qui est déjà créée"""
        serialized_player = {
            'name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
            'rank': self.rank}
        db = tinyDB('../Models/PlayerDatabase.json')
        table = db.table('Joueurs')
        table.insert(serialized_player)
