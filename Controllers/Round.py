#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Controllers.Tournament import add_player_to_tournament


def generate_first_round(player_on_tournament):
    """
    Trier les joueurs par rank
    """
    sorted_list = sorted(player_on_tournament, key=lambda joueurs: joueurs[2])
    # print(sorted_list)
    result = list()
    number_round = 1
    if number_round == 1:
        match_1 = (sorted_list[0], sorted_list[4])
        match_2 = (sorted_list[1], sorted_list[5])
        match_3 = (sorted_list[2], sorted_list[6])
        match_4 = (sorted_list[3], sorted_list[7])
        match_list = [match_1, match_2, match_3, match_4]
        score(match_list)

        number_round = number_round + 1
    elif number_round == 2:



def score():
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

            result.append((i + 1, match_list[i][j], score_match))

def rank_of_tournament():
    points =

def save_round():
    pass
