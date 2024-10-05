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
        crit_limit = 12 if move_info['name'] == 'Razor Leaf' else 5
        crit = 2 if random.randint(0, 100) <= crit_limit else 1
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
            if hit_chance >= random.randint(0, 100):
                return True
            else:
                return False

    def _status_move(self, attack, pokemon1, pokemon2, damage, priority):

        if priority:
            if attack['name'] in ['Growl']:
                pokemon2.attackstage = pokemon2.attackstage - 1 if pokemon2.attackstage > -6 else pokemon2.attackstage
                if pokemon2.attackstage < 0:
                    pokemon2.currentattack = round(pokemon2.attack * self.debuff[(pokemon2.attackstage * -1) - 1])
                elif pokemon2.attackstage > 0:
                    pokemon2.currentattack = round(pokemon2.attack * self.buff[pokemon2.attackstage - 1])
                else:
                    pokemon2.currentattack = pokemon2.attack

            elif attack['name'] in ['Growth']:
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
            elif attack['name'] in ['Sweet Scent']:
                pokemon2.evasionstage = pokemon2.evasionstage - 1 if pokemon2.evasionstage > -6 else pokemon2.evasionstage

            elif attack['name'] in ['Smokescreen']:
                pokemon2.accuracystage = pokemon2.accuracystage - 1 if pokemon2.accuracystage > -6 else pokemon2.accuracystage

            elif attack['name'] in ['Scary Face']:
                pokemon2.speedstage = pokemon2.speedstage - 1 if pokemon2.speedstage > -6 else pokemon2.speedstage
                if pokemon2.speedstage < 0:
                    pokemon2.currentspeed = round(pokemon2.speed * self.debuff[(pokemon2.speedstage * -1) - 1])
                elif pokemon2.speedstage > 0:
                    pokemon2.currentspeed = round(pokemon2.speed * self.buff[pokemon2.speedstage - 1])
                else:
                    pokemon2.currentspeed = pokemon2.speed

            elif attack['name'] in ['Poison Powder']:
                if not pokemon2.statuscondition:
                    pokemon2.statuscondition = "Poisoned"
                else:
                    print("O ataque não teve efeito")

            elif attack['name'] in ['Sleep Powder']:
                if not pokemon2.statuscondition:
                    pokemon2.statuscondition = "Sleeping"
                    pokemon2.sleepcount = random.randint(1, 4)
                else:
                    print("O ataque não teve efeito")

        else:
            if attack['name'] in ['Take Down']:
                rebound_damage = round(damage / 4)
                pokemon1.currenthp -= rebound_damage 
                print (f'{pokemon1.name} sofreu {rebound_damage} de recuo.')

            elif attack['name'] in ['Ember', 'Fire Blast', 'Fire Fang', 'Fire Punch', 'Flame Wheel', 'Flamethrower', 'Flare Blitz', 'Heat Wave']:
                if random.randint(0, 100) <= 10 and not pokemon2.statuscondition:
                    pokemon2.statuscondition = "Burned"
                    print(f"O {pokemon2.name} foi queimado!")


        return pokemon1, pokemon2




    def battleRound(self, pokemon1, pokemon2, attack_1, attack_2):
        round_count = 0

        if pokemon1.statuscondition == "Sleeping":
            print(f"O {pokemon1.name} está dormindo.")

        elif self.accuracy_check(attack_1["accuracy"], pokemon1.accuracystage, pokemon2.evasionstage):
            print("#" * 30)
            print(f"{pokemon1.name} primeiro usou {attack_1['name']}")

            # calculo do primeiro ataque

            pokemon1, pokemon2 = self._status_move(attack_1, pokemon1, pokemon2, 0, True)

            damage_1 = 0
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

            pokemon1, pokemon2 = self._status_move(attack_1, pokemon1, pokemon2, damage_1, False)

        else:
            print("#" * 30)
            print(f"{pokemon1.name} primeiro usou {attack_1['name']}")
            print(f"{pokemon1.name} errou!")

        # calculo do segundo ataque

        if pokemon2.statuscondition == "Sleeping":
            print(f"O {pokemon2.name} está dormindo.")

        elif self.accuracy_check(attack_2["accuracy"], pokemon2.accuracystage, pokemon1.evasionstage):
            print("#" * 30)
            print(f"{pokemon2.name} segundo usou {attack_2['name']}")

            pokemon2, pokemon1 = self._status_move(attack_2, pokemon2, pokemon1, 0, True)

            damage_2 = 0
            if attack_2['kind'] in ['Physical', 'Special']:
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
            pokemon2, pokemon1 = self._status_move(attack_2, pokemon2, pokemon1, damage_2, False)

        else:
            print("#" * 30)
            print(f"{pokemon2.name} segundo usou {attack_2['name']}")
            print(f"{pokemon2.name} errou!")
            print("#" * 30)

        round_count += 1

        # Verificação Status Pokemon 1
        if pokemon1.statuscondition == "Poisoned":
            poison_damage = round(pokemon1.hp / 8)
            pokemon1.healthdamage(poison_damage)
            print(f"{pokemon1.name} sofreu {poison_damage} de dano por envenenamento")

        elif pokemon1.statuscondition == "Burned":
            burn_damage = round(pokemon1.hp / 16)
            pokemon1.healthdamage(burn_damage)
            print(f"{pokemon1.name} sofreu {burn_damage} de dano por queimadura")

        elif pokemon1.statuscondition == "Sleeping":
            if pokemon1.sleepcount > 0:
                pokemon1.sleepcount -= 1
            else:
                pokemon1.statuscondition = ''
                print(f"{pokemon1.name} acordou!")

        # Verificação Status Pokemon 2
        if pokemon2.statuscondition == "Poisoned":
            poison_damage = round(pokemon2.hp / 8)
            pokemon2.healthdamage(poison_damage)
            print(f"{pokemon2.name} sofreu {poison_damage} de dano por envenenamento")

        elif pokemon2.statuscondition == "Burned":
            burn_damage = round(pokemon2.hp / 16)
            pokemon2.healthdamage(burn_damage)
            print(f"{pokemon2.name} sofreu {burn_damage} de dano por queimadura")

        elif pokemon2.statuscondition == "Sleeping":
            if pokemon2.sleepcount > 0:
                pokemon2.sleepcount -= 1
            else:
                pokemon2.statuscondition = ''
                print(f"{pokemon2.name} acordou!")


        poke1_porcentagem = pokemon1.currenthp / pokemon1.hp if pokemon1.currenthp > 0 else 0
        hash_amount = round(poke1_porcentagem * 10)
        dash_amount = 10 - hash_amount

        print('|', '#'*hash_amount, '-'*dash_amount, '| ', 'Hp do ', pokemon1.name,  sep='' )


        poke2_porcentagem = pokemon2.currenthp / pokemon2.hp if pokemon2.currenthp > 0 else 0
        hash_amount = round(poke2_porcentagem * 10)
        dash_amount = 10 - hash_amount

        print('|', '#'*hash_amount, '-'*dash_amount, '| ', 'Hp do ', pokemon2.name,  sep='' )
       


