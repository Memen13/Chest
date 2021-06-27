import re

def new_date(a_word):
    while True:
        date = input(f"Indiquez la date {a_word} au format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", date)) == 0:
            print("La date indiquée est au mauvais format")
        else:
            return date

def tournament_rules(kind):
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