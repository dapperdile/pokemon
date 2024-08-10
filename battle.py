import random

class Pokemon_battle:
    def __init__(self, types_matchup, types):
        self.types_matchup = types_matchup
        self.types = types
        self.buff = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0] # Stages 1 até 6
        self.debuff = [0.67, 0.5, 0.4, 0.33, 0.29, 0.25] # Stages -1 até -6
        self.eva_accbuff = [1.33, 1.67, 2, 2.33, 2.66, 3] # Stages 1 até 6
        self.eva_accdebuff = [0.75, 0.6, 0.5, 0.43, 0.38, 0.33] # Stages -1 até -6

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

        return 0 if move_power == 0 else damage, crit==2, matchup>=2

    def accuracy_check(self, accuracy, pokemon1_accurary, pokemon2_evasion):
        if pokemon1_accurary > 0:
            p_attacker = self.eva_accbuff[pokemon1_accurary - 1]
        elif pokemon1_accurary < 0:
            p_attacker = self.eva_accdebuff[pokemon1_accurary + 1]
        else:
            p_attacker = 1

        if pokemon2_evasion > 0:
            eva_rival = self.eva_accbuff[pokemon2_evasion - 1]
        elif pokemon2_evasion < 0:
            eva_rival = self.eva_accdebuff[pokemon2_evasion + 1]
        else:
            eva_rival = 1

        if accuracy == "-":
            return True

        else:
            hit_chance = round((int(accuracy) * p_attacker) / eva_rival)
            hit_chance = hit_chance if hit_chance <= 100 else 100
            print('----------TESTE HIT CHANGE', hit_chance)
            if hit_chance >= random.randint(0, 100):
                return True
            else:
                return False

    def battleRound(self, pokemon1, pokemon2, attack_1, attack_2):
        print("#" * 30)
        print(f"{pokemon1.name} primeiro usou {attack_1['name']}")
        if self.accuracy_check(attack_1["accuracy"], pokemon1.accuracystage, pokemon2.evasionstage):

            # calculo do primeiro ataque
            if attack_1['kind'] in ['Physical', 'Special']:
                attack_points = pokemon1.currentattack if attack_1['kind'] == 'Physical' else pokemon1.currentsattack
                defense_points = pokemon2.currentdefense if attack_1['kind'] == 'Physical' else pokemon2.currentsdefense

                damage_1, is_crit_2, is_matchup_2 = self.damageCalculation(pokemon1.lvl, attack_1, attack_points, defense_points, pokemon1.poke_type, pokemon1.poke_type2, 
                pokemon2.poke_type, pokemon2.poke_type2)
                if is_crit_2:
                    print('Foi um ataque crítico!')

                if is_matchup_2:
                    print('Foi um ataque super efetivo')

                print(f"Acertou com {damage_1:.0f} de dano!")
                print("#" * 30)
                pokemon2.healthdamage(round(damage_1))
                print(f'A vida do {pokemon2.name} é {pokemon2.currenthp}')
                print("#" * 30)

            elif attack_1['name'] in ['Growl']:
                pokemon2.attackstage = pokemon2.attackstage - 1 if pokemon2.attackstage > -6 else pokemon2.attackstage
                if pokemon2.attackstage < 0:
                    pokemon2.currentattack = round(pokemon2.attack * self.debuff[(pokemon2.attackstage * -1) - 1])
                elif pokemon2.attackstage > 0:
                    pokemon2.currentattack = round(pokemon2.attack * self.buff[pokemon2.attackstage - 1])
                else:
                    pokemon2.currentattack = pokemon2.attack

            elif attack_1['name'] in ['Growth']:
                # print(f'------Teste sattack {pokemon1.sattack}')
                # print(f'------Teste sattackstage {pokemon1.sattackstage}')
                pokemon1.sattackstage = pokemon1.sattackstage + 1 if pokemon1.sattackstage < 6 else pokemon1.sattackstage
                if pokemon1.sattackstage < 0:
                    pokemon1.currentsattack = round(pokemon1.sattack * self.debuff[(pokemon1.sattackstage * -1) - 1])
                elif pokemon1.sattackstage > 0:
                    pokemon1.currentsattack = round(pokemon1.sattack * self.buff[pokemon1.sattackstage - 1])
                else:
                    pokemon1.currentsattack = pokemon1.sattack
                # print(f'------Teste sattackstage {pokemon1.sattackstage}')
                # print(f'------Teste currentsattack {pokemon1.currentsattack}')
            elif attack_1['name'] in ['Sweet Scent']:
                print('------------TESTE POKEMON 2 EVASION', pokemon2.evasionstage)
                pokemon2.evasionstage = pokemon2.evasionstage - 1 if pokemon2.evasionstage > -6 else pokemon2.evasionstage
                print('------------TESTE POKEMON 2 EVASION 2', pokemon2.evasionstage)



        else:
            print(f"{pokemon1.name} errou!")

        # calculo do segundo ataque
        print("#" * 30)
        print(f"{pokemon2.name} segundo usou {attack_2['name']}")
        if self.accuracy_check(attack_2["accuracy"], pokemon2.accuracystage, pokemon1.evasionstage):
            attack_points = pokemon2.currentattack if attack_2['kind'] == 'Physical' else pokemon2.currentsattack
            defense_points = pokemon1.currentdefense if attack_2['kind'] == 'Physical' else pokemon1.currentsdefense

            damage_2, is_crit_1, is_matchup_1 = self.damageCalculation(pokemon2.lvl, attack_2, attack_points, defense_points, pokemon2.poke_type, pokemon2.poke_type2, 
            pokemon1.poke_type, pokemon1.poke_type2)
            if is_crit_1:
                print('Foi um ataque crítico!')

            if is_matchup_1:
                print('Foi um ataque super efetivo')

            print(f"Acertou com {damage_2:.0f} de dano!")
            print("#" * 30)
            pokemon1.healthdamage(round(damage_2))
            print(f'A vida do {pokemon1.name} é {pokemon1.currenthp}')
            print("#" * 30)

        else:
            print(f"{pokemon2.name} errou!")
            print("#" * 30)