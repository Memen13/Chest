#!/usr/bin/env python
# -*- coding: utf-8 -*-

from View.Recurrent import *


def player_menu_view():
    Recurrent.user_choice()
    while True:
        choice = input("""1: Créer un nouveau joueur\n 2: Voir les joueurs enregistrés\n 3: Rechercher un joueur\n 
                        4: Modifier un joueur \n 5: Revenir au menu principal""")
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3
        elif choice == "4":
            return 4
        elif choice == "5":
            return 5
        else:
            Recurrent.unknow_choice()
            player_menu_view()

