import os
import csv
import pprint
from pokemon_obj import Pokemon_char
from battle import Pokemon_battle

__author__ = "rafael.bernardo"
__date__ = "04/05/2024"
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
    notvalidate = True
    while notvalidate:
        pokemon1 = input("Digite o nome do primeiro Pokemon: ")
        pokechoice1, pokechoice1name = pokenameValidation(pokemon1, pokelist)
        if len(pokechoice1) > 1:
            pokemon1 = input(f"Selecione o pokemon {pokechoice1name}: ")
            for index, pokechname in enumerate(pokechoice1name):
                if pokemon1 == pokechname:
                    pokemon1 = pokechoice1[index]
                    notvalidate = False
                    break
        elif len(pokechoice1) == 1:
            pokemon1 = pokechoice1[0]
            break
        else:
            print("Nome incorreto")

    notvalidate = True
    while notvalidate:
        pokemon2 = input("Digite o nome do segundo Pokemon: ")
        os.system("cls")
        pokechoice2, pokechoice2name = pokenameValidation(pokemon2, pokelist)
        if len(pokechoice2) > 1:
            pokemon2 = input(f"Selecione o pokemon {pokechoice2name}: ")
            for index, pokechname in enumerate(pokechoice2name):
                if pokemon2 == pokechname:
                    pokemon2 = pokechoice2[index]
                    notvalidate = False
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
    print()


    moveslearning = []
    for row in lvllist:
        if row[0] == pokename and int(row[1]) <= lvl:
            moveslearning.append(row[2])
    print('Possiveis movimentos: \n')
    print(moveslearning, "\n")
    
    moveslearned = [] if len(moveslearning) > 4 else moveslearning
    while len(moveslearned) < 4 and moveslearned != moveslearning:
        move = input("Digite o movimento do Pokemon: ")
        if move in moveslearning:
            moveslearned.append(move)
        else:
            print('Movimento incorreto')
    os.system("cls")

    
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
            
    return movesinfo, lvl


# Tratamento dos dados
file = open('data/pokemon.csv')
csvreader = csv.reader(file)

file = open('data/tipagem.csv')
csvtipagem = csv.reader(file)

file = open('data/poke_move_lvl_processed.csv')
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
poke_1_moves, lvlpoke1 = pokeMoveInput(pokemon1[1], pokemovelist, pokemoves)
poke_2_moves, lvlpoke2 = pokeMoveInput(pokemon2[1], pokemovelist, pokemoves)

pokemon1 = Pokemon_char(pokemon1, lvlpoke1, moves=poke_1_moves)
pokemon2 = Pokemon_char(pokemon2, lvlpoke2, moves=poke_2_moves)

print(pokemon1.name,' vs ', pokemon2.name)

for move in pokemon1.moves:
    print (move["name"], "|", move["effect"], "|", move["type"], "|", move["kind"], "|", move["pp"])
        

battle_state = True
while battle_state:
    

    if pokemon1.currenthp > 0 and pokemon2.currenthp > 0:
        # escolher movimentos
        for move in pokemon1.moves:
            print (move["name"], "|", move["effect"], "|", move["type"], "|", move["kind"], "|", move["pp"])
        
        # verificar o movimento escolhido
        wrong_input = True
        while wrong_input: 
            attack = input("Digite o nome do movimento: ")
            attack_validation = pokemon1.moveValidation(attack)
            if attack_validation == True:
                wrong_input = False
                print('movimento validado')
            else:
                print("Nome incorreto")
        
    elif pokemon1.currenthp > 0 and pokemon2.currenthp == 0:
        print(f'{pokemon1.name} venceu {pokemon2.name}')
        battle_state = False
    
    elif pokemon1.currenthp == 0 and pokemon2.currenthp > 0:
        print(f'{pokemon2.name} venceu {pokemon1.name}')
        battle_state = False
    
    else:
        print ('Os dois pokemons foram derrotados!')
        battle_state = False

