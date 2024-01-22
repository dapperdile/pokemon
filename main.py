import csv

__author__ = "diogo.shiroto"
__date__ = "21/01/2024"
__version__ = open("version").readline()

file = open('pokemon.csv')
csvreader = csv.reader(file)

file = open('Tipagem.csv')
csvtipagem = csv.reader(file)

print(csvtipagem)

types_matchup = []

for row in csvtipagem:
    types_matchup.append(row)



rows = []
for row in csvreader:
    rows.append(row[1:4])
    

rows = rows[1:]

types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]

pokemon1 = rows[0]
pokemon2 = rows[6]
print(pokemon1,' vs ', pokemon2)

