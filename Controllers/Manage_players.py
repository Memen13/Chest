#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Models.Players import PlayerModel

class ManagePlayers():

""" Class permettant d'ajouter des joueurs"""

    def add_players():

        player = PlayerModel

        player.first_name = input("Prénom du joueur: ")
        player.last_name = input("Nom du joueur: ")
        player.age = input("Âge du joueur: ")
        player.gender = input("Sexe du joueur: ")
        player.rank = input("Elo du joueur: ")
        player.id = input("Entrez l'id du joueur")
