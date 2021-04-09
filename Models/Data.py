#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query, where


class DataTournament():
    """
        Class générale héritée sur les autres models afin de gérer la base de donnée

        """
    def __init__(self,objectTournament):
        self.objectTournament = objectTournament
        self.db = TinyDB(self.objectTournament.name + '.json')
        self.table = self.db.table("Tournois")

    def update(self):
        self.table.insert({"name" : self.objectTournament.name})

    def delete(self, number):
         self.table.remove({"id" : number)

    def search(self):
        table = Data.db.table(self.__class__.__name__)
        Data.get()

    def load(self):

class DataPlayer():

    def __init__(self,objectTournament):
        self.objectTournament = objectTournament
        self.db = TinyDB(self.objectTournament.name + '.json')
        self.table = self.db.table("Tournois")

    def update(self):
        self.table.insert({"name" : self.objectTournament.name})