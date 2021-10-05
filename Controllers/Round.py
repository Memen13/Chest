#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Controllers.Tournament import *


class Round:
    def __init__(self):

    def make_a_round(self):




























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
