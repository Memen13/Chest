#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from Models import Data


class TournamentModel(Data):
    """

    Model du tournois qui définit les paramètre à prendre en compte pour la création ou le chargement de tournois

    """

    def __init__(self, name, location, d_start, d_end, kind, description, number_of_players, result, player_id):
        self.name = name
        self.location = location
        self.d_start = d_start.strftime("%A %d. %B %Y")
        self.d_end = d_end.strftime("%A %d. %B %Y")
        self.kind = kind
        self.description = description
        self.rounds = 4
        self.number_of_players = int(number_of_players)
        self.result = result
        self.player_id = int(player_id)
