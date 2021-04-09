#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Models.Tournament import TournamentModel

class CreateTournament():
     print("Un nouveau tournois a été créé!")
     def new_tournament():

        tournois = TournamentModel()

         tournois.name = input("Nom du tournois:")
         tournois.location = input("Lieu du tournois:")
         tournois.d_start = input("Date du début du tournois:")
         tournois.d_end = input("Date de la fin du tournois:")
         tournois.kind = input("Type de tournois: ")
         tournois.description = input("Description du tournois:")
         tournois.rounds = ("Nombre de round = 4")
         tournois.number_of_players = input("Entrez le nombre de joueurs:")
         tournois.id = input("Entrez les id des joueurs")

response = int(input("Souhaitez-vous débuter un nouveau tournois? \n1 \n2"))

if response == 1:
    CreateTournament()
else:
    print("C'est dommage!")




"""

Quand le tournois est créé:
1: Créer la liste des matchs
2: Faire une première sauvegarde= Créer la méthode pour save
3: Entrer les résultats et ajouter les points (0/0.5/1) 
4  Prpoposer à l'utilisateur de sauvegarder à chaque nouveau round (joueur + tournois)
5: Indiquer la fin du tournois

"""
