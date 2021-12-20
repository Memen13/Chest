#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from Controllers.Tournament import add_player_to_tournament

class Round:
   """docstring"""
    def __init__(self, name, date, time_start,time_end,match_list):
        self.name = name
        self.date = date.today.strftime("%d/%m/%Y")
        self.time_start = time_start.time.now()
        self.time_end = time_end.time.now()
        self.match_list = []

    def generate_first_round(player_on_tournament):
        """
        Trier les joueurs par rank

        """
        sorted_list = sorted(player_on_tournament, key=lambda joueurs: joueurs[2])
        print(sorted_list)
        match_1 = (sorted_list[0], sorted_list[4])
        match_2 = (sorted_list[1], sorted_list[5])
        match_3 = (sorted_list[2], sorted_list[6])
        match_4 = (sorted_list[3], sorted_list[7])
        match_list = [match_1, match_2, match_3, match_4]
        result = list()

        for i in range(0, 4):
            print(f"Le match en cours oppose {match_list[i][0]} à {match_list[i][1]}")
            for j in range(0, 2):
                while True:
                    try:
                        score_match = float(input(f"""Le match est terminé!
                                                  Veillez indiquer le score de {match_list[i][j]}"""))
                        break
                    except:
                        print("""Le score est incorrect. Veuillez indiquer un des ces scores:
                         1 point = Victoire; 0,5 point = Match nul; 0 point = défaite""")

                result.append((i, match_list[i][j], score_match))






    def generate_round(self):
        pass

    def save_round(self):
        pass


round = Round()
round.generate_first_round(add_player_to_tournament())


























sorted_list = [
    ('Federer', 3, 12),
    ('Djockovich', 2, 12),
    ('Nadal', 1, 10),
]

# Classement par points
sorted_list = sorted(sorted_list, key=lambda joueurs: joueurs[1])

print("Trie par rank :", sorted_list)

sorted_list = sorted(sorted_list, key=lambda joueurs: joueurs[2], reverse=True)

print("Trie par points :", sorted_list)
