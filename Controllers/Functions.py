import re
import json

import db as db
from tinydb import tinyDB, Query, where

from Controllers.Tournois import name


def new_date(a_word):
    while True:
        date = input(f"Indiquez la date {a_word} au format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}) =$/", date)= 0:
            print("La date indiquée est au mauvais format")
        else:
            return date

def tournament_rules():
    while True:
        kind = input("Règles du tournois:\nPour Blitz, tapez 1\nPour Bullet, tapez 2\nPour Coup Rapide, tapez 3")

        if kind == "1":
            new_kind = "Blitz"
            break
        elif kind == "2":
            new_kind = "Bullet"
            break
        elif kind == "3":
            new_kind == "Coup Rapide"
            break
        else:
            print("Votre choix n'est pas reconnu. Veuillez recommencer")

def player_json():
    with open('PlayerDatabase.json') as json_data_player:
        data_dict = json.load(json_data_player)
        print(str(data_dict).replace("{", '').replace("}", ''))

def search_id():
    player_id = name.search(where('type') == 'name')

    player_seek = input("Indiquez le nom de joueur que vous recherchez")
    player = Query()
    db.search(player.name == player_seek)

def add_player()
    with open('PlayerDatabase.json') as json_data_player:
        player_for_tournament = input("Veuillez indiquer l'id du joueur que vous souhaitez intégrer au tournois")
    db.get(player_for_tournament)


    """d_start = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
    if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_start)) == 0:
        print("La date indiquée est au mauvais format")"""
