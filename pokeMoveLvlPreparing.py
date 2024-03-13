import csv

file = open('data/poke_move_lvl_raw.csv')
csvmovelvl = csv.reader(file) 

pokemovelist = []
for row in csvmovelvl:
    pokemovelist.append(row)

for row in pokemovelist:
    try:
        int(row[0])
        isint = True
    except:
        isint = False
    if isint == False and row[0] not in ["Evo.", "Rem."]:
        poke_name = row[0]
    print(poke_name)
        
        
