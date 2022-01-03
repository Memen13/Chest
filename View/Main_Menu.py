#!/usr/bin/env python
# -*- coding: utf-8 -*-


from View import Recurrent
from View.Manage_tournament import *
from View.Manage_players import *


def welcome():
    print("""
    ------------------------------------------------------
    ******************************************************
    BIENVENUE SUR L'APPLICATION TOURNOIS D'ECHECS
    ******************************************************
    ------------------------------------------------------""")

    choice = input("Choisir 1 pour continuer, ou 2 pour quitter")
    while True:
        if choice == "1":
            main_page()
        elif choice == "2":
            exit()

def main_page():
    Recurrent.user_choice()
    print("------------------------------------------------------")
    choice = input("1: Voir le menu principal\n 2: Quitter l'application ")
    print("------------------------------------------------------")
    while True:
        if choice == "1":
            main_menu()
        elif choice == "2":
            exit()
        else:
            Recurrent.unknow_choice()
            main_page()

def main_menu():
    Recurrent.user_choice()
    choice = input("1: Voir le menu des tournois\n 2: Voir le menu des joueurs\n 3: Quitter")
    while True:
        if choice == "1":
            tournament_menu()
        elif choice == "2":
            manage_player_content()
        elif choice == "3":
            exit()
        else:
            Recurrent.unknow_choice()
            main_menu()
