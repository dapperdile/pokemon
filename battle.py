import random

class Pokemon_battle:
    def __init__(self, types_matchup, types):
        self.types_matchup = types_matchup
        self.types = types
    
    def __typeAdvantage(self, attack, defense, defense1):
        index_attack = None
        index_defense = None
        index_defense1 = None

        for index, valor in enumerate(self.types):
            if valor == attack:
                index_attack = index
            if valor == defense:
                index_defense = index
            if valor == defense1:
                index_defense1 = index

        if index_defense1: 
            
            result = float(self.types_matchup[index_attack][index_defense]) * float(self.types_matchup[index_attack][index_defense1])
        else:
            result = float(self.types_matchup[index_attack][index_defense])

        return result


    def attackValidation(self, input_attack):
        validation = False
        index = self.types.index(input_attack)
        if index >= 0:
            validation = True

        return validation


    def damageCalculation(self, lvl, move_info, attack, defense, poke_1_type_1, poke_1_type_2, 
                          poke_2_type_1, poke_2_type_2):
        crit = 2 if random.randint(0, 100)  <= 5  else  1
        rand = random.randint(217, 255) / 255
        stab = 1.5 if move_info["type"] == poke_1_type_1 or poke_1_type_2 else 1
        matchup = self.__typeAdvantage(move_info['type'], poke_2_type_1, poke_2_type_2)
        move_power = int(move_info['power']) if move_info['power'].isdigit() else 0
        calculate_crit = (((2 * lvl * crit)/5) + 2)
        raw_damage = ((calculate_crit * move_power * ((attack / defense))/50) + 2)
        
        damage = raw_damage * stab * matchup * rand

        return 0 if move_power == 0 else damage