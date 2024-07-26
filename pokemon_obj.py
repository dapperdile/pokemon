import random

class Pokemon_char:
	def __init__(self, pokemon, lvl=1, moves=[]):
		self.IVhp = random.randint(0, 31)
		self.IVattack = random.randint(0, 31)
		self.IVdeffence = random.randint(0, 31)
		self.IVsattack = random.randint(0, 31)
		self.IVsdeffence = random.randint(0, 31)
		self.IVspeed = random.randint(0, 31)
		self.name = pokemon[1]
		self.poke_type = pokemon[2]
		self.poke_type2 = pokemon[3]
		self.lvl = lvl
		self.moves = moves
		self.hp = round((int(pokemon[4]) + self.IVhp)/4) + 2 * lvl
		self.attack = round((int(pokemon[5]) + self.IVattack)/9) + lvl
		self.deffence = round((int(pokemon[6]) + self.IVdeffence)/9) + lvl
		self.sattack = round((int(pokemon[7]) + self.IVsattack)/9) + lvl
		self.sdeffence = round((int(pokemon[8]) + self.IVsdeffence)/9) + lvl
		self.speed = round((int(pokemon[9]) + self.IVspeed)/9) + lvl
		self.currenthp = self.hp
		self.currentattack = self.hp
		self.attackstage = 0
		self.currentdeffense = self.hp
		self.deffensestage = 0
		self.currentsattack = self.hp
		self.sattackstage = 0
		self.currentsdeffense = self.hp
		self.sdeffensestage = 0
		self.currentspeed = self.hp
		self.speedstage = 0
		self.accuracystage = 0


	def moveValidation(self, move):
		for mv in self.moves:
			if mv["name"] == move:
				return True, mv
		return False, None

	def healthdamage(self, damage):
		self.currenthp -= damage
