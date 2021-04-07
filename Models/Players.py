# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Models.Data import Data

class PlayerModel(Data):
    """

    Model qui gère les paramètre définis et à définir des joueurs

    """

    def __init__(self, id, first_name, last_name, age, gender, rank, tournament_points):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.rank = int(rank)
        self.tournament_points = int(tournament_points)
