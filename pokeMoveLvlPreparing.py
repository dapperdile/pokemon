import csv

__author__ = "rafael.bernardo"
__date__ = "12/03/2024"
__version__ = open("version").readline()

file = open('data/poke_move_lvl_raw.csv')
csvmovelvl = csv.reader(file) 

pokemovelist = []
for row in csvmovelvl:
    pokemovelist.append(row)

result = []
for row in pokemovelist:
    try:
        int(row[0])
        isint = True    
    except:
        isint = False

    if isint == False and row[0] not in ["Evo.", "Rem."]:
        poke_name = row[0]
    else:
        result.append([poke_name, row[0], row[1]])

with open('data/poke_move_lvl_processed.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)