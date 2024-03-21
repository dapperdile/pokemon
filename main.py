import csv
from pokemon_obj import Pokemon_char
from battle import Pokemon_battle

__author__ = "rafael.bernardo"
__date__ = "20/03/2024"
__version__ = open("version").readline()


types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]
battle = Pokemon_battle()

def pokenameValidation(input_name, pokelist):
    pokechoice = []
    pokechoicename = []
    for poke in pokelist:
        if input_name in poke[1]:
            pokechoice.append(poke)
            pokechoicename.append(poke[1])
            
    
    return pokechoice, pokechoicename

def pokeInput(pokelist):
    while True:
        pokemon1 = input("Digite o nome do primeiro Pokemon: ")
        pokechoice1, pokechoice1name = pokenameValidation(pokemon1, pokelist)
        if len(pokechoice1) > 1:
            pokemon1 = input(f"Selecione o pokemon {pokechoice1name}: ")
            for index, pokechname in enumerate(pokechoice1name):
                if pokemon1 == pokechname:
                    pokemon1 = pokechoice1[index]
                    break
        elif len(pokechoice1) == 1:
            pokemon1 = pokechoice1[0]
            break
        else:
            print("Nome incorreto")

    while True:
        pokemon2 = input("Digite o nome do segundo Pokemon: ")
        pokechoice2, pokechoice2name = pokenameValidation(pokemon2, pokelist)
        if len(pokechoice2) > 1:
            pokemon2 = input(f"Selecione o pokemon {pokechoice2name}: ")
            for index, pokechname in enumerate(pokechoice2name):
                if pokemon2 == pokechname:
                    pokemon2 = pokechoice2[index]
                    break
        elif len(pokechoice2) == 1:
            pokemon2 = pokechoice2[0]
            break
        else:
            print("Nome incorreto")
    
    return pokemon1, pokemon2

def pokeMoveInput(pokename, lvllist, movelist):
    str_question = "Digite o level do Pokemon " + pokename + ": "
    while True:
        lvl = int(input(str_question))
        if 0 < lvl < 101:
            break
        else:
            print("Valor do level incorreto")
            


    moveslearning = []
    for row in lvllist:
        if row[0] == pokename and int(row[1]) <= lvl:
            moveslearning.append(row[2])
    print('Possiveis movimentos: ', moveslearning)
    

    moveslearned = [] if len(moveslearning) > 4 else moveslearning
    while len(moveslearned) < 4:
        move = input("Digite o movimento do Pokemon: ")
        if move in moveslearning:
            moveslearned.append(move)
        else:
            print('Movimento incorreto')

    
    movesinfo = []
    for move in moveslearned:
        for moveinfo in movelist:
            if move == moveinfo[0]:
                movesinfo.append({
                    "name": moveinfo[0],
                    "effect": moveinfo[1],
                    "type": moveinfo[2],
                    "kind": moveinfo[3],
                    "power": moveinfo[4],
                    "accuracy": moveinfo[5],
                    "pp": moveinfo[6]
                })

                break
            
    return movesinfo


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
    row.pop(4)
    pokelist.append(row[0:10])
pokelist = pokelist[1:]

pokemovelist = []
for row in csvmovelvl:
    pokemovelist.append(row)
pokemovelist = pokemovelist[1:]    

pokemoves = []
for row in csvmoves:
    pokemoves.append(row[1:])
pokemoves = pokemoves[2:]


# Identificação dos Pokemons
pokemon1, pokemon2 = pokeInput(pokelist)

# Preparando pokemons
poke_1_moves = pokeMoveInput(pokemon1[1], pokemovelist, pokemoves)
poke_2_moves = pokeMoveInput(pokemon2[1], pokemovelist, pokemoves)

pokemon1 = Pokemon_char(pokemon1, lvl=1, moves=poke_1_moves)
pokemon2 = Pokemon_char(pokemon2, lvl=1, moves=poke_2_moves)


print(pokemon1.name,' vs ', pokemon2.name)

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
