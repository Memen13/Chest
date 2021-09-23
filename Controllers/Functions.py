import re
import json
from tinydb import tinyDB, Query, where

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
        new_tournament.d_start = new_date("de début du tournois, ")
    elif choice == 4:
        new_tournament.d_end = new_date("de fin du tournois,")
    elif choice == 5:
        new_tournament.kind = tournament_rules()
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
        change_tournament_info()

def new_date(a_word):
    while True:
        date = input(f"Indiquez la date {a_word} au format JJ/MM/AAAA")
        if len(re.findall("/^\d{2}-\d{2}-\d{4}) =$/", date)=0:
            print("La date indiquée est au mauvais format")
            """raise ValueError"""
        else:
            return date

def tournament_rules():
    while True:
        kind = input("Règles du tournois:\nPour Blitz, tapez 1\nPour Bullet, tapez 2\nPour Coup Rapide, tapez 3")

        if kind == "1":
            new_kind = "Blitz"
            break
        elif kind == "2":
            new_kind = "Bullet"
            break
        elif kind == "3":
            new_kind == "Coup Rapide"
            break
        else:
            print("Votre choix n'est pas reconnu. Veuillez recommencer")

def player_json():
    with open('PlayerDatabase.json') as json_data_player:
        data_dict = json.load(json_data_player)
        print(str(data_dict).replace("{", '').replace("}", ''))

def tournament_json():
    with open('TournamentDatabase.json') as json_tournament:
        data_tournament = json.load(json_tournament)
        print(str(data_tournament).replace("{", '').replace("}", ''))


def search_by_tournament_name():

    tournament_seek = input ("Indiquez le nom du tournois que vous recherchez")
    tournament = Query()
    result = db.table('TournamentDatabase.json').search(tournament.name == tournament_seek)
    print(result)

def search_by_player_name():
    """docstring"""

    player_seek = input("Indiquez le nom de joueur que vous recherchez")
    player = Query()
    result = db.table('Players').search(player.name == player_seek)
    print(result)

def change_player(new_player):
    while True:
        choice = input("Que souhaitez-vous modifier? \n 1 : Le prénom\n 2 :Le nom\n 3 : L'âge\n 4 : Sexe\n"
                       "5 : Elo du joueur")
        if choice == 1:
            new_player_name = input("Indiquez le nouveau prénom:")
            new_player.first_name = new_player_name
        elif choice == 2:
            new_last_name = input("Indiquez le nouveau nom:")
            new_player.last_name = new_last_name
        elif choice == 3:
            new_age = input(int("Indiquez l'âge du joueur:"))
            new_player.age = new_age
        elif choice == 4:
            new_gender = input("Indiquez l'âge du joueur:")
            new_player.gender = new_gender
        elif choice == 5:
            new_rank = input(int("Indiquez le nouvel Elo du joueur"))
            new_player.rank = new_rank


    """d_start = input("Indiquez la date du début du tournois (format JJ/MM/AAAA")
    if len(re.findall("/^\d{2}-\d{2}-\d{4}$/", d_start)) == 0:
        print("La date indiquée est au mauvais format")"""
