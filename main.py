import csv

__author__ = "rafael.vasconcelos"
__date__ = "21/01/2024"
__version__ = open("version").readline()

file = open('pokemon.csv')
csvreader = csv.reader(file)

file = open('Tipagem.csv')
csvtipagem = csv.reader(file)


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

attack = "Flying"
defense = pokemon1[1]
defense1 = pokemon1[2]

print(defense, defense1)

index_attack = None
index_defense = None
index_defense1 = None

for index,valor in enumerate(types):
    if valor == attack:
        index_attack = index
    elif valor == defense:
        index_defense = index
    elif valor == defense1:
        index_defense1 = index

result = int(types_matchup[index_attack][index_defense]) * int(types_matchup[index_attack][index_defense1])


print (result)

