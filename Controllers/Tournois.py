#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Tournament:
    def __init__(self, id, name, localisation, d_start, d_end, kind, description, round = 4):
        self.id = id
        self.name = name
        self.localisation = localisation
        self.d_start = d_start
        self.d_end = d_end
        self.round = round
        self.kind = kind
        self.description = description

        print(f'Le tournois {self.name} a été créé')


# Transformer en class
# verifier le type de l'objet et faire appel à la méthode modification du tournois (same pour players) (récupérer depuis le json tinydb)
def change_tournois(new_tournament):
    while True:
        choice = input("Que voulez vous mettre à jour ? \n 1 : Le nom\n 2 : La localisation\n 3 : La date du début\n"
                       "4 : La date de fin \n 5: Les règles du tournois\n 6 : La description")
        if choice == 1:
            new_name = input("Indiquez le nouveau nom")
            new_tournament.name = new_name
        elif choice == 2:
            new_localisation = input("Indiquez la nouvelle localisation")
            new_tournament.localisation = new_localisation
        elif choice == 3:
            while True:
                new_dstart = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
                if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_start)) == 0:
                    print("La date indiquée est au mauvais format")
                else:
                    new_tournament.d_start = new_dstart
        elif choice == 4:
            while True:
                new_dend = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
                if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_end)) == 0:
                    print("La date indiquée est au mauvais format")
                else:
                    new_tournament.d_end = new_dend
        elif choice == 5:
            pass
        elif choice == 6:
            new_description = input("Renseignez la nouvelle description du tournois")
            new_tournament.description = new_description

        elif choice == 7:
            print("Très bien, ne changeons rien!")
            break

        other_choice = input("Voulez vous modifier autre chose ? Tapez Oui ou Non")
        if other_choice.lower() == "non":
            break
        elif other_choice.lower() == "oui":
            pass
        # Que se passe-t-il si "oui"

creation_tournament = input("Voulez vous créer un tournois ? Tapez Oui ou Non")
if creation_tournament.lower() == "oui":
    id = 1

    name = input("Indiquez le nom du tournois")
    localisation = input("Indiquez la localisation")
    # L'utilisateur doit indiquer la date au format définit par le programme
    while True:
        d_start = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_start)) == 0:
            print("La date indiquée est au mauvais format")
        else:
            break
    while True:
        d_end = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_end)) == 0:
            print("La date indiquée est au mauvais format")
        else:
            break
   while True:
            kind = input("Règles du tournois:\nPour Blitz, tapez 1\nPour Bullet, tapez 2\nPour Coup Rapide, tapez 3")

            if kind == "1":
                kind = "Blitz"
                break
            elif kind == "2":
                kind = "Bullet"
                break
            elif kind == "3":
                kind == "Coup Rapide"
                break
            else:
                print("Votre choix n'est pas reconnu. Veuillez recommencer")

    description = input("Renseignez la description du tournois")


new_tournament = Tournament(id, name, localisation, d_start, d_end, kind, description, round)
    choix = input("Voulez vous modifier quelque chose ? Tapez oui ou non")
    if choix.lower() == "oui":
        change_tournois(new_tournament)
    else:
        print("Ce sera pour une prochaine fois")


def majObjet(choice):
  import re
  if choice == 3:
    while True:
      d_start = input("Indiquez la date du début du tournois (format JJ-MM-AAAA")
      if len(re.findall("^\d{2}-\d{2}-\d{4}$", d_start)) == 0:
          print("La date indiquée est au mauvais format")
      else:
          new_d_start = d_start
          return new_d_start
          #break
  else:
    print("Choix inconnu")


majObjet(3)
def majDate(texte):
  while True:
    date = input(f"Indiquez la date {texte} (format JJ-MM-AAAA)")
    if len(re.findall("^\d{2}-\d{2}-\d{4}$", date)) == 0:
        print("La date indiquée est au mauvais format")
    else:
        new_date = date
        return new_date

    class Objet:
        def __init__(self):
            self.date = "01-01-2021"

    new_objet = Objet()
    print(new_objet.date)

def majObjet(choix):
        print("Pour mettre à jour la date tapez 1, pour quitter taper Q")
        if choix == "1":
            new_objet.date = majDate("du début du tournois")

    majObjet("1")
    print(new_objet.date)