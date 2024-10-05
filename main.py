import time
import os
import csv
import json
import random
import log__ as log
from datetime import datetime
from pokemon_obj import Pokemon_char
from battle import Pokemon_battle

__author__ = "rafael.bernardo"
__date__ = "04/10/2024"
__version__ = open("version").readline()
__project__ = "Pokemon"


timestamp = datetime.now().strftime("%Y-%m-%dT%H_%M_%S")
types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]
poke1random = False
poke2random = False
move1random = False
move2random = False

def pokenameValidation(input_name, pokelist):
    pokechoice = []
    pokechoicename = []
    for poke in pokelist:
        if input_name in poke[1].capitalize():
            pokechoice.append(poke)
            pokechoicename.append(poke[1])


    return pokechoice, pokechoicename

def pokeInput(pokelist, random_allow_1=False, random_allow_2=False):
    if not random_allow_1:
        notvalidate = True
        while notvalidate:
            pokemon1 = input("Digite o nome do primeiro Pokemon: ")
            os.system("cls")
            pokechoice1, pokechoice1name = pokenameValidation(pokemon1.capitalize(), pokelist)
            if len(pokechoice1) > 1:
                pokemon1 = input(f"Selecione o pokemon {pokechoice1name}: ")
                for index, pokechname in enumerate(pokechoice1name):
                    if pokemon1.capitalize() == pokechname.capitalize():
                        pokemon1 = pokechoice1[index]
                        notvalidate = False
                        break
            elif len(pokechoice1) == 1:
                pokemon1 = pokechoice1[0]
                break
            else:
                print("Nome incorreto")

    else:
        pokemon1 = random.choices(pokelist)[0]

    if not random_allow_2:
        notvalidate = True
        while notvalidate:
            pokemon2 = input("Digite o nome do segundo Pokemon: ")
            os.system("cls")
            pokechoice2, pokechoice2name = pokenameValidation(pokemon2.capitalize(), pokelist)
            if len(pokechoice2) > 1:
                pokemon2 = input(f"Selecione o pokemon {pokechoice2name}: ")
                for index, pokechname in enumerate(pokechoice2name):
                    if pokemon2.capitalize() == pokechname.capitalize():
                        pokemon2 = pokechoice2[index]
                        notvalidate = False
                        break
            elif len(pokechoice2) == 1:
                pokemon2 = pokechoice2[0]
                break
            else:
                print("Nome incorreto")
    else:
        pokemon2 = random.choices(pokelist)[0]

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

        moveslearning = [row[2] for row in lvllist if row[0] == pokename 
                         and (row[1] in ["Evo.", "Rem."] 
                              or (row[1].isdigit() and int(row[1]) <= lvl))]
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

        moveslearning = [row[2] for row in lvllist if row[0] == pokename 
                         and (row[1] in ["Evo.", "Rem."] 
                              or (row[1].isdigit() and int(row[1]) <= lvl))]

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

def movePriority(prioritylist, move1, move2, speed1, speed2):
    validation = True
    while validation:
        # for move, value in prioritylist.items():
        #     inpriority.append(move)
        if move1 in prioritylist and move2 in prioritylist:
            value1 = int(prioritylist[move1])
            value2 = int(prioritylist[move2])
            if value1 > value2:
                return 1
            elif value1 < value2:
                return 2
            elif speed1 > speed2:
                return 1
            elif speed1 < speed2:
                return 2
            else: 
                return random.choices([move1, move2])[0]
        elif move1 in prioritylist:
            return 2 if int(prioritylist[move1]) < 0 else 1
        elif move2 in prioritylist :
            return 1 if int(prioritylist[move2]) < 0 else 2
        elif speed1 > speed2:
            return 1
        else:
            return 2

try:
    log_poke = log.log(__project__, __version__, timestamp)

    log_poke.internal(log_name="import-pokemons-data", timestamp=timestamp) # Início do log
    # Tratamento dos dados
    file = open('data/pokemon.csv')
    csvreader = csv.reader(file)

    file = open('data/tipagem.csv')
    csvtipagem = csv.reader(file)

    file = open('data/poke_move_lvl_processed.csv')
    csvmovelvl = csv.reader(file)

    file = open('data/poke_moves_new.csv')
    csvmoves = csv.reader(file)
    log_poke.internal_finish(log_name="import-pokemons-data", success=True) # Fechamento do log

    log_poke.internal(log_name="data-treatment", timestamp=timestamp) # Início do log

    with open('data/poke_move_priority.json', 'r', encoding='utf8') as file:
        prioritymoves = json.load(file)

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

    log_poke.internal_finish(log_name="data-treatment", success=True) # Fechamento do log

    log_poke.internal(log_name="battle-initialization", timestamp=timestamp) # Início do log
    battle = Pokemon_battle(types_matchup, types)
    log_poke.internal_finish(log_name="battle-initialization", success=True) # Fechamento do log

    log_poke.internal(log_name="pokemon-moves-input", timestamp=timestamp) # Início do log
    # Identificação dos Pokemons
    pokemon1, pokemon2 = pokeInput(pokelist, random_allow_1=poke1random, random_allow_2=poke2random)
    print(pokemon1)

    # Preparando pokemons
    poke_1_moves, lvlpoke1 = pokeMoveInput(pokemon1[1], pokemovelist, pokemoves, move1random)
    poke_2_moves, lvlpoke2 = pokeMoveInput(pokemon2[1], pokemovelist, pokemoves, move2random)

    log_poke.internal_finish(log_name="pokemon-moves-input", success=True, result=[pokemon1, pokemon2]) # Fechamento do log

    log_poke.internal(log_name="pokemon-initialization", timestamp=timestamp) # Início do log
    pokemon1 = Pokemon_char(pokemon1, lvlpoke1, moves=poke_1_moves)
    pokemon2 = Pokemon_char(pokemon2, lvlpoke2, moves=poke_2_moves)
    log_poke.internal_finish(log_name="pokemon-initialization", success=True) # Fechamento do log

    print(pokemon1.name,' vs ', pokemon2.name)

    log_poke.internal(log_name="battle-start", timestamp=timestamp) # Início do log
    battle_state = True
    while battle_state:
        if pokemon1.currenthp > 0 and pokemon2.currenthp > 0:
            # escolher movimentos
            for move in pokemon1.moves:
                print (move["name"], "|", move["effect"],
                        "|", move["type"], "|", move["kind"], "|", move["pp"], move["power"])

            # attack_1 = random.choices(pokemon1.moves)[0]
            wrong_input = True
            while wrong_input: 
                attack_1_str = input("Digite o nome do movimento: ").title()
                attack_validation, move_poke1 = pokemon1.moveValidation(attack_1_str)
                if attack_validation == True:
                    wrong_input = False
                    print('movimento validado')
                else:
                    print("Nome incorreto")
            for move in pokemon1.moves:
                if move['name'] == attack_1_str:
                    attack_1 = move
                    break

            # escolha aleatoria do movimento do segundo pokemon
            attack_2 = random.choices(pokemon2.moves)[0]
            
            # execução do ataque em ordem de velocidade do pokemon
            attackpriority = movePriority(prioritymoves, attack_1['name'], attack_2['name'],
                                        pokemon1.currentspeed, pokemon2.currentspeed)
            if attackpriority == 1:
                battle.battleRound(pokemon1, pokemon2, attack_1, attack_2)
            else:
                battle.battleRound(pokemon2, pokemon1, attack_2, attack_1)
            time.sleep(1)
        elif pokemon1.currenthp > 0 and pokemon2.currenthp <= 0:
            print(f'{pokemon1.name} venceu {pokemon2.name}')
            battle_state = False

        elif pokemon1.currenthp <= 0 and pokemon2.currenthp > 0:
            print(f'{pokemon2.name} venceu {pokemon1.name}')
            battle_state = False

        else:
            print ('Os dois pokemons foram derrotados!')
            battle_state = False
    log_poke.internal_finish(log_name="battle-start", success=True,
                             result=[pokemon1.name, pokemon1.currenthp,
                                     pokemon2.name, pokemon2.currenthp]) # Fechamento do log

except Exception as ex:
    print("steps_error = ", log_poke.show_steps_error())
    print("Error: ", ex)

finally:
    log_poke.save()

