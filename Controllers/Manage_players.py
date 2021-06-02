#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Player():
"""
docstring
 """
    def __init__(self):
        while True:
            self.first_name = input("Prénom du joueur: ")
            self.last_name = input("Nom du joueur: ")
            self.age = input("Âge du joueur: ")
            self.gender = input("Sexe du joueur: ")
            self.rank = input("Elo du joueur: ")

            print(f' Voici les informations du joueur: \n
            - First name : {self.first_name}\n Souhaitez-vous valider votre sélection?")
            choice = input("Tapez 1 pour oui ou 2 pour non)
            if choice == "1":
                break



"""-Créer joueur et le stocker dans la bdd
