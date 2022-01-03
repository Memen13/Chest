#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from Controllers.Tournament import add_player_to_tournament

class Round:
   """docstring"""
    def __init__(self, name, date, time_start,time_end,match_list):
        self.name = name
        self.date = date.today.strftime("%d/%m/%Y")
        self.time_start = time_start.time.now()
        self.time_end = time_end.time.now()


def save_round():
    """ Model for save a round"""
    pass

