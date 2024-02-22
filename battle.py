class Pokemon_battle:
    def __init__(self):
        self.id = None
    
    
    def typeAdvantage(self, attack, defense, defense1, types_matchup, types):
        index_attack = None
        index_defense = None
        index_defense1 = None

        for index,valor in enumerate(types):
            if valor == attack:
                index_attack = index
            if valor == defense:
                index_defense = index
            if valor == defense1:
                index_defense1 = index

        if index_defense1: 
            result = int(types_matchup[index_attack][index_defense]) * int(types_matchup[index_attack][index_defense1])
        else:
            result = int(types_matchup[index_attack][index_defense])

        return result


    def pokenameValidation(self, input_name, pokelist):
        pokeinfo = None
        validation = False
        for poke in pokelist:
            if input_name == poke[1]:
                validation = True
                pokeinfo = poke
                break
        
        return validation, pokeinfo


    def attackValidation(self, input_attack, types):
        validation = False
        index = types.index(input_attack)
        if index >= 0:
            validation = True
        
        return validation
