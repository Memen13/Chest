#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Tournament:
    def __init__(self, id, name, localisation, d_start, d_end, kind, description, round = 4):
        self.id = id
        self.name = name
        self.localisation = localisation
        self.d_start = d_start
        self.d_end = d_end
        self.round = round
        self.kind = kind
        self.description = description

        print(f'Le tournois {self.name} a été créé')



def change_tournois(new_tournament):
    while True:
        choice = input("Que voulez vous mettre à jour ? \n 1 : Le nom\n 2 : La localisation")
        if choice == 1:
            new_name = input("Indiquez le nouveau nom")
            new_tournament.name = new_name
        elif choice == 2:
            new_localisation = input("Indiquez la nouvelle localisation")
            new_tournament.localisation = new_localisation
        else:
            other_choice = input("Voulez vous modifiez autre chose ? Tapez Oui ou Non")
            if other_choice.lower() == "non":
                break
            elif other_choice.lower() == "oui":
                pass


"""print("Bienvenue dans notre programme")"""
creation_tournament = input("Voulez vous créer un tournois ? Tapez Oui ou Non")
if creation_tournament.lower() == "oui":
    id = 1

    name = input("Indiquez le nom du tournoi")
    localisation = input("Indiquez la localisation")
    #L'utilisateur doit indiquer la date au format définit par le programme
    while True:
        d_start = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_start)) == 0:
            print("La date indiquée est au mauvais format")
        else:
            break
    while True:
        d_end = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_end)) == 0:
            print("La date indiquée est au mauvais format")
        else:
            break
   while True:
            kind = input("Règles du tounrnois:\nPour Blitz, tapez 1\nPour Bullet, tapez 2\nPour Coup Rapide, tapez 3")

            if kind == "1":
                kind = "Blitz"
                break
            elif kind == "2":
                kind = "Bullet"
                break
            elif kind == "3":
                kind == "Coup Rapide"
                break
            else:
                print("Votre choix n'est pas reconnu. Veuillez recommencer")












new_tournament = Tournament(id, name, localisation, d_start, d_end, round, kind, description)
    choix = input("Voulez vous modifier quelque chose ? Tapez oui ou non")
    if choix.lower() == "oui":
        change_tournois(new_tournament)
else:
    print("Ce sera pour une prochaine fois")