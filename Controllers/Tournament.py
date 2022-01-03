#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Models.Data_Tournament import Tournament
from View.Manage_tournament import *
from View.Recurrent import *
import pprint
from datetime import *
from tinydb import TinyDB, Query


def tournament_menu_controller():

    """docstring"""

    user_choice = tournament_menu_view()
    if user_choice == 1:
        Tournament()
    elif user_choice == 2:
        show_tournament_data()
    elif user_choice == 3:
        content_tournament()
    elif user_choice == 4:
        main_menu()

def add_player_to_tournament():

    """ Fonction qui permet l'incrustation de joueurs dans le tournois depuis la base de donnée."""

    cpt = 1
    # Pour que l'id soit indiqué sur la ligne 96 sur l'input
    players_list = list()
    while True:
        choice = input("Connaissez vous les Id des joueurs que vous voulez ? Oui ou Non").upper()
        if choice == "OUI":
            while True:
                id = int(input(f"Merci d'indiquer l'id du joueur {cpt} :"))
                players_list.append((db.get(doc_id=id)["name"], db.get(doc_id=id)["last_name"],
                                     db.get(doc_id=id)["rank"]))
                cpt = cpt + 1
                if cpt == 9:
                    break
            break
        elif choice == "NON":
            print("Ci-dessous ")
            print(db.all())
            while True:
                id = int(input(f"Merci d'indiquer l'id du joueur {cpt} :"))
                players_list.append((db.get(doc_id=id)["name"], db.get(doc_id=id)["last_name"]))
                if cpt == 9:
                    break
            break
        else:
            Recurrent.unknow_choice()
            add_player_to_tournament()
    return players_list

def tournament_rules():

    """Méthode permettant le choix des règles pour le tournois."""

    while True:
        choice = input("Règles du tournois:\nPour Blitz, tapez 1\nPour Bullet, tapez 2\nPour Coup Rapide, tapez 3")

        if choice == "1":
            kind = "Blitz"
            break
        elif choice == "2":
            kind = "Bullet"
            break
        elif choice == "3":
            kind = "Coup Rapide"
            break
        else:
            Recurrent.unknow_choice()
            tournament_rules()
    return kind


def show_tournament_data():

    """ Méthode afin de voir la bdd des tournois existants """

    db = TinyDB('TournamentDatabase.json')
    tournament = db.table('Tournament')
    pprint(tournament.all())

def content_tournament():

    """ Méthode afin de vérifier les informations d'n tournois déjà existant """

    tournament_seek = input("Indiquez le nom du tournois que vous recherchez")
    tournament = Query()
    result = db.table('TournamentDatabase.json').search(tournament.name == tournament_seek)
    print(result)