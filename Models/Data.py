#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query, where


class Data():
    """
    Class générale héritée sur les autres models afin de gérer la base de donnée

    """

    db = TinyDB('data/db.json')

    def save(self, data):
        table = Data.db.table(self.__class__.__name__)
        Data.db.insert(self.__dict__)

    def update(self):
        table = Data.db.table(self.__class__.__name__)
        query = Query()
        table.update(self)

    def delete(self):
        table = Data.db.table(self.__class__.__name__)
        query = Query()
        table.remove()

    def search(self):
        table = Data.db.table(self.__class__.__name__)
        Data.get()

