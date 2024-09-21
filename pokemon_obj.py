import random

class Pokemon_char:
	def __init__(self, pokemon, lvl=1, moves=[]):
		self.IVhp = random.randint(0, 31)
		self.IVattack = random.randint(0, 31)
		self.IVdefense = random.randint(0, 31)
		self.IVsattack = random.randint(0, 31)
		self.IVsdefense = random.randint(0, 31)
		self.IVspeed = random.randint(0, 31)
		self.name = pokemon[1]
		self.poke_type = pokemon[2]
		self.poke_type2 = pokemon[3]
		self.lvl = lvl
		self.moves = moves
		self.hp = round((int(pokemon[4]) + self.IVhp)/4) + 2 * lvl
		self.attack = round((int(pokemon[5]) + self.IVattack)/9) + lvl
		self.defense = round((int(pokemon[6]) + self.IVdefense)/9) + lvl
		self.sattack = round((int(pokemon[7]) + self.IVsattack)/9) + lvl
		self.sdefense = round((int(pokemon[8]) + self.IVsdefense)/9) + lvl
		self.speed = round((int(pokemon[9]) + self.IVspeed)/9) + lvl
		self.currenthp = self.hp
		self.currentattack = self.attack
		self.attackstage = 0
		self.currentdefense = self.defense
		self.defensestage = 0
		self.currentsattack = self.sattack
		self.sattackstage = 0
		self.currentsdefense = self.sdefense
		self.sdefensestage = 0
		self.currentspeed = self.speed
		self.speedstage = 0
		self.accuracystage = 0
		self.evasionstage = 0
		self.statuscondition = ''


	def moveValidation(self, move):
		for mv in self.moves:
			if mv["name"] == move:
				return True, mv
		return False, None

	def healthdamage(self, damage):
		self.currenthp -= damage
