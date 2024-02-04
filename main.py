import csv
from pokemon_obj import pokemon_char
from battle import Pokemon_battle

__author__ = "diogo.shiroto"
__date__ = "24/01/2024"
__version__ = open("version").readline()

poke_1_moves = [{
    "name": "Tackle",
    "type": "Normal",
    "category": "Physical",
    "power": 40,
    "accuracy": 1,
    "pp": 35
},
{
    "name": "Growl",
    "type": "Normal",
    "category": "Status",
    "power": None,
    "accuracy": 1,
    "pp": 40
}]

pokemon1 = pokemon_char(dex_number=1, poke_type='grass', lvl=1, moves=poke_1_moves)
print("----- TESTE 1 pokemon1 = ",  pokemon1.poke_type)

battle = Pokemon_battle()


# Tratamento dos dados
file = open('pokemon.csv')
csvreader = csv.reader(file)

file = open('Tipagem.csv')
csvtipagem = csv.reader(file)

types_matchup = []

for row in csvtipagem:
    types_matchup.append(row)

pokelist = []
for row in csvreader:
    pokelist.append(row[1:4])
    
pokelist = pokelist[1:]

types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]

# Identificação dos Pokemons

wrong_input = True
while wrong_input:
    pokemon1 = input("Digite o nome do primeiro Pokemon: ")
    poke_validation, pokemon1 = battle.pokenameValidation(pokemon1, pokelist)
    if poke_validation == True:
        wrong_input = False
    else:
        print("Nome incorreto")

wrong_input = True
while wrong_input:
    pokemon2 = input("Digite o nome do segundo Pokemon: ")
    poke_validation, pokemon2 = battle.pokenameValidation(pokemon2, pokelist)
    if poke_validation == True:
        wrong_input = False
    else:
        print("Nome incorreto")


print(pokemon1,' vs ', pokemon2)

wrong_input = True
while wrong_input:
    attack = input("Digite o tipo do ataque: ")
    attack_validation = battle.attackValidation(attack, types)
    if attack_validation == True:
        wrong_input = False
    else:
        print("Nome incorreto")

defense = pokemon2[1]
defense1 = pokemon2[2]

result = battle.typeAdvantage(attack, defense, defense1, types_matchup, types)

print("Multiplicação de dano = ", result)
