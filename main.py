import csv

__author__ = "diogo.shiroto"
__date__ = "21/01/2024"
__version__ = open("version").readline()

file = open('pokemon.csv')
csvreader = csv.reader(file)

rows = []
for row in csvreader:
    rows.append(row[1:4])

rows = rows[1:]

types_matchup = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]

