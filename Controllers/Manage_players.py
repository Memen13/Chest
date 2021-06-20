#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Models.Data_players import *

class Players:
    """
        docstring
    """

    def __init__(self):
        while True:
            self.first_name = input("Prénom du joueur: ")
            self.last_name = input("Nom du joueur: ")
            self.age = input(int("Âge du joueur: "))
            while True:
                self.gender = input("Sexe du joueur: 1: M 2: F")
                if self.gender == "1":
                    self.gender = "Masculin"
                    break
                elif self.gender == "2":
                    self.gender = "Féminin"
                    break
            self.rank = input(int("Elo du joueur: "))

            print(f""" Voici les informations du joueur:
            - Prénom: {self.first_name}
            -Nom: {self.last_name}
            -Âge: {self.age}
            -Sexe: {self.gender}:
            -Elo du joueur: {self.rank}
            Souhaitez-vous modifier une information?""")
            choice = input("Tapez 1 pour oui ou 2 pour non")
            if choice == "1":
                return change_player
            else:
                break

        def save_player():
            """ Add le joueur à la bdd qui est déjà créée"""
            serialized_player = {
                'name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
                'gender': self.gender,
                'rank': self.rank}
            insert(serialized_player)

    def change_player(new_player):
        while True:
            choice = input("Que souhaitez-vous modifier? \n 1 : Le prénom\n 2 :Le nom\n 3 : L'âge\n 4 : Sexe\n"
                           "5 : Elo du joueur")
            if choice == 1:
                new_player_name = input("Indiquez le nouveau prénom:")
                new_player.first_name = new_player_name
            elif choice == 2:
                new_last_name = input("Indiquez le nouveau nom:")
                new_player.last_name = new_last_name
            elif choice == 3:
                new_age = input(int("Indiquez l'âge du joueur:"))
                new_player.age = new_age
            elif choice == 4:
                new_gender = input("Indiquez l'âge du joueur:")
                new_player.gender = new_gender
            elif choice == 5:
                new_rank = input(int("Indiquez le nouvel Elo du joueur"))
                new_player.rank = new_rank

