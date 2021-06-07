#!/usr/bin/env python
# -*- coding: utf-8 -*-



    def update(self, objectTournament):
        self.table.insert({"name": objectTournament.name})

    def delete(self, number):
         self.table.remove({"id" : number)

    def load(self):

