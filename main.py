import csv
from pokemon_obj import Pokemon_char
from battle import Pokemon_battle

__author__ = "rafaeleao"
__date__ = "21/02/2024"
__version__ = open("version").readline()


types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]
battle = Pokemon_battle()

def pokeInput(battle, pokelist):

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
    
    return pokemon1, pokemon2

# Tratamento dos dados
file = open('data/pokemon.csv')
csvreader = csv.reader(file)

file = open('data/tipagem.csv')
csvtipagem = csv.reader(file)

file = open('data/poke_move_lvl.csv')
csvmovelvl = csv.reader(file)

file = open('data/poke_moves.csv')
csvmoves = csv.reader(file)

types_matchup = []
for row in csvtipagem:
    types_matchup.append(row)

pokelist = []
for row in csvreader:
    pokelist.append(row[0:4])
pokelist = pokelist[1:]

pokemovelist = []
for row in csvmovelvl:
    pokemovelist.append(row)
pokemovelist = pokemovelist[1:]    

pokemoves = []
for row in csvmoves:
    row.pop(2)
    pokemoves.append(row[1:])
pokemoves = pokemoves[2:]


print(pokemoves)
# Identificação dos Pokemons
pokemon1, pokemon2 = pokeInput(battle, pokelist)   


# Preparando pokemons
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

pokemon1 = Pokemon_char(dex_number=1, poke_type='grass', lvl=1, moves=poke_1_moves)
print("----- TESTE 1 pokemon1 = ",  pokemon1.poke_type)

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
