#!/usr/bin/env python
# -*- coding: utf-8 -*-



    def update(self, objectTournament):
        self.table.insert({"name": objectTournament.name})

    def delete(self, number):
         self.table.remove({"id" : number)

    def load(self):

class DataPlayer():

    def __init__(self):
         self.db = TinyDB('PlayerDatabase.json')
         self.table = self.db.table("Players")

    def update(self):
        self.table.insert({"name" : self.objectTournament.name})