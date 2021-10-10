#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Controllers.Tournament import *


class Round:
    def __init__(self, round_number=4, match):
        self.round_number = round_number
        # Générer 4 matchs par round depuis la fonction spécifique
        self.match = match

    def add_score(self):































joueurs_tuples = [
    ('Federer', 3, 12),
    ('Djockovich', 2, 12),
    ('Nadal', 1, 10),
]

# Classement par points
joueurs_tuples = sorted(joueurs_tuples, key=lambda joueurs: joueurs[1])

print("Trie par rank :", joueurs_tuples)

joueurs_tuples = sorted(joueurs_tuples, key=lambda joueurs: joueurs[2], reverse=True)

print("Trie par points :", joueurs_tuples)
