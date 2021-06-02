# !/usr/bin/env python
# -*- coding: utf-8 -*-


class PlayerModel():
    """

    Model qui gère les paramètre définis et à définir des joueurs

    """

    def __init__(self, id, first_name, last_name, age, gender, rank):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.rank = int(rank)

    def tournament_points(self):
        self.tournament_points = tournament_points

    def update_rank(self, new_rank):
        self.rank = new_rank

    neymar.update_rank(32)
    neymar.rank