#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB


class DataTournament():
    """
        data tournois

        """

    def __init__(self):
        """
        self.objectTournament = objectTournament
        """

        self.db = TinyDB('TournoisDataBase.json')
        self.table = self.db.table("Tournois")

    def update(self, objectTournament):
        self.table.insert({"name": objectTournament.name})



