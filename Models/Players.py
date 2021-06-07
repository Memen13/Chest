# !/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB


class PlayerModel():
    """

    Docstring

    """

    class DataPlayer():

        def __init__(self):
            self.db = TinyDB('PlayerDatabase.json')
            self.table = self.db.table("Players")

        def update(self):
            self.table.insert({"name": self.objectTournament.name})

            # récupérer l'id

    def tournament_points(self):
        self.tournament_points = tournament_points

    def update_rank(self, new_rank):
        self.rank = new_rank


