import os
import csv
import random
from pokemon_obj import Pokemon_char
from battle import Pokemon_battle

__author__ = "janio.almeida"
__date__ = "23/05/2024"
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
        os.system("cls")
        pokechoice1, pokechoice1name = pokenameValidation(pokemon1.capitalize(), pokelist)
        if len(pokechoice1) > 1:
            pokemon1 = input(f"Selecione o pokemon {pokechoice1name}: ")
            for index, pokechname in enumerate(pokechoice1name):
                if pokemon1.capitalize() == pokechname:
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
        pokechoice2, pokechoice2name = pokenameValidation(pokemon2.capitalize(), pokelist)
        if len(pokechoice2) > 1:
            pokemon2 = input(f"Selecione o pokemon {pokechoice2name}: ")
            for index, pokechname in enumerate(pokechoice2name):
                if pokemon2.capitalize() == pokechname:
                    pokemon2 = pokechoice2[index]
                    notvalidate = False
                    break
        elif len(pokechoice2) == 1:
            pokemon2 = pokechoice2[0]
            break
        else:
            print("Nome incorreto")

    return pokemon1, pokemon2

def pokeMoveInput(pokename, lvllist, movelist, random_allow = False):
    if random_allow == False:
        str_question = "Digite o level do Pokemon " + pokename + ": "
        while True:
            lvl = int(input(str_question))
            if 0 < lvl < 101:
                break
            else:
                print("Valor do level incorreto")
        print()

        moveslearning = [row[2] for row in lvllist if row[0] == pokename and (row[1] == "Evo." or int(row[1]) <= lvl)]
        print('Possiveis movimentos: \n')
        print(moveslearning, "\n")

        moveslearned = [] if len(moveslearning) > 4 else moveslearning
        while len(moveslearned) < 4 and len(moveslearned) != len(moveslearning):
            move = input("Digite o movimento do Pokemon: ")
            if move.title() in moveslearning:
                moveslearned.append(move.title())
            else:
                print('Movimento incorreto')
        os.system("cls")


    else:
        lvl = random.randint(1,100)

        moveslearning = [row[2] for row in lvllist if row[0] == pokename and (row[1] == "Evo." or int(row[1]) <= lvl)]

        moveslearned = [] if len(moveslearning) > 4 else moveslearning

        moveslearning_aux = moveslearning
        while len(moveslearned) < 4 and len(moveslearned) != len(moveslearning):
            move = random.choices(moveslearning_aux)[0]
            moveslearned.append(move)
            moveslearning_aux.remove(move)

    movesinfo = []
    for move in moveslearned:
        for moveinfo in movelist:
            if move == moveinfo[0]:
                movesinfo.append({
                    "name": moveinfo[0],
                    "effect": moveinfo[6],
                    "type": moveinfo[1],
                    "kind": moveinfo[2],
                    "power": moveinfo[3],
                    "accuracy": moveinfo[4],
                    "pp": moveinfo[5]
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

file = open('data/poke_moves_new.csv')
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
    pokemoves.append(row)
pokemoves = pokemoves[1:]


# Identificação dos Pokemons
pokemon1, pokemon2 = pokeInput(pokelist)

# Preparando pokemons
poke_1_moves, lvlpoke1 = pokeMoveInput(pokemon1[1], pokemovelist, pokemoves)
poke_2_moves, lvlpoke2 = pokeMoveInput(pokemon2[1], pokemovelist, pokemoves, True)

pokemon1 = Pokemon_char(pokemon1, lvlpoke1, moves=poke_1_moves)
pokemon2 = Pokemon_char(pokemon2, lvlpoke2, moves=poke_2_moves)

print(pokemon1.name,' vs ', pokemon2.name)


battle_state = True
while battle_state:
    if pokemon1.currenthp > 0 and pokemon2.currenthp > 0:
        # escolher movimentos
        for move in pokemon1.moves:
            print (move["name"], "|", move["effect"], "|", move["type"], "|", move["kind"], "|", move["pp"])

        # verificar o movimento escolhido
        wrong_input = True
        while wrong_input: 
            attack_1 = input("Digite o nome do movimento: ").title()
            attack_validation = pokemon1.moveValidation(attack_1)
            if attack_validation == True:
                wrong_input = False
                print('movimento validado')
            else:
                print("Nome incorreto")

        # escolha aleatoria do movimento do segundo pokemon
        attack_2 = random.choices(pokemon2.moves)[0]['name']
        
        # execução do ataque em ordem de velocidade do pokemon
        if pokemon1.speed > pokemon2.speed:
            print(pokemon1.speed, pokemon2.speed)
            print(f"{pokemon1.name} usou {attack_1}")
            print(f"{pokemon2.name} usou {attack_2}")
        else:
            print(pokemon1.speed, pokemon2.speed)
            print(f"{pokemon2.name} usou {attack_2}")
            print(f"{pokemon1.name} usou {attack_1}")

    elif pokemon1.currenthp > 0 and pokemon2.currenthp == 0:
        print(f'{pokemon1.name} venceu {pokemon2.name}')
        battle_state = False

    elif pokemon1.currenthp == 0 and pokemon2.currenthp > 0:
        print(f'{pokemon2.name} venceu {pokemon1.name}')
        battle_state = False

    else:
        print ('Os dois pokemons foram derrotados!')
        battle_state = False
