#!/usr/bin/env python
# -*- coding: utf-8 -*-

joueurs_tuples = [
    ('Federer', 3, 12),
    ('Djockovich', 2, 12),
    ('Nadal', 1, 10),
]

# Classement par points
joueurs_tuples = sorted(joueurs_tuples, key=lambda joueurs: joueurs[1])

print("Trie par rand :", joueurs_tuples)

joueurs_tuples = sorted(joueurs_tuples, key=lambda joueurs: joueurs[2], reverse=True)

print("Trie par points :", joueurs_tuples)