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
    

    def battleRound(self, pokemon1, pokemon2, attack_1, attack_2):
        # calculo do primeiro ataque
            print("#" * 30)
            print(f"{pokemon1.name} primeiro usou {attack_1['name']}")

            attack_points = pokemon1.attack if attack_1['kind'] == 'Physical' else pokemon1.sattack
            defense_points = pokemon2.deffence if attack_1['kind'] == 'Physical' else pokemon2.sdeffence

            damage_2 = self.damageCalculation(pokemon1.lvl, attack_1, attack_points,
                                                defense_points, pokemon1.poke_type, pokemon1.poke_type2, 
                                                pokemon2.poke_type, pokemon2.poke_type2)
            print(f"Acertou com {damage_2:.0f} de dano!")

            # calculo do segundo ataque
            print("#" * 30)
            print(f"{pokemon2.name} segundo usou {attack_2['name']}")

            attack_points = pokemon2.attack if attack_2['kind'] == 'Physical' else pokemon2.sattack
            defense_points = pokemon1.deffence if attack_2['kind'] == 'Physical' else pokemon1.sdeffence

            damage_1 = self.damageCalculation(pokemon2.lvl, attack_2, attack_points, 
                                                defense_points, pokemon2.poke_type, pokemon2.poke_type2, 
                                                pokemon1.poke_type, pokemon1.poke_type2)
            print(f"Acertou com {damage_1:.0f} de dano!")
            print("#" * 30)

            print(f'vida atual {pokemon2.currenthp}')
            pokemon2.healthdamage(round(damage_2))
            print(f'a vida do {pokemon2.name} é {pokemon2.currenthp}')