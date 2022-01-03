#!/usr/bin/env python
# -*- coding: utf-8 -*-


from View.Main_Menu import *
from View.Recurrent import *
from Controllers.Tournament import *
from View.Recurrent import user_choice


def tournament_menu_view(tournament_menu_controller):
    Recurrent.user_choice()
    while True:
        choice = input("1: Créer un nouveau tournois\n 2: Voir les tournois enregistrés\n 3: Charger un tournois\n "
                       "4: Revenir au menu principal")
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3
        elif choice == "4":
            return 4
        else:
            Recurrent.unknow_choice()
            tournament_menu_view()

