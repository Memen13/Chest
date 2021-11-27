#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from tinydb import tinyDB, Query, TinyDB


def player_json():
    db = TinyDB('PlayerDatabase.json')
    players = db.table('Players')
    pprint(players.all())

def search_by_player_name():
    player_seek = input("Indiquez le nom du joueur que vous recherchez")
    player = Query()
    result = db.table('PlayerDatabase.json').search(player.name == player_seek)
    print(result)

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
