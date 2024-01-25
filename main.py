import csv

__author__ = "rafael.vasconcelos"
__date__ = "24/01/2024"
__version__ = open("version").readline()

def typeAdvantage(attack, defense, defense1, types_matchup, types):
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
    
    return result


def pokenameValidation(input_name, pokelist):
    pokeinfo = None
    validation = False
    for poke in pokelist:
        if input_name == poke[0]:
            validation = True
            pokeinfo = poke
            break
    
    return validation, poke


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
    poke_validation, pokemon1 = pokenameValidation(pokemon1, pokelist)
    if poke_validation == True:
        wrong_input = False
    else:
        print("Nome incorreto")    

wrong_input = True
while wrong_input:
    pokemon2 = input("Digite o nome do segundo Pokemon: ")
    poke_validation, pokemon2 = pokenameValidation(pokemon2, pokelist)
    if poke_validation == True:
        wrong_input = False
    else:
        print("Nome incorreto")   


print(pokemon1,' vs ', pokemon2)

wrong_input = True
while wrong_input:
    pokemon2 = input("Digite o nome do segundo Pokemon: ")
    poke_validation, pokemon2 = pokenameValidation(pokemon2, pokelist)
    if poke_validation == True:
        wrong_input = False
    else:
        print("Nome incorreto") 

defense = pokemon1[1]
defense1 = pokemon1[2]

print(defense, defense1)

result = typeAdvantage(attack, defense, defense1, types_matchup, types)

print(result)