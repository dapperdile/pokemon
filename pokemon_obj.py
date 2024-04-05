class Pokemon_char:
	def __init__(self, pokemon, lvl=1, moves=[]):
		self.name = pokemon[1]
		self.poke_type = pokemon[2]
		self.poke_type2 = pokemon[3]
		self.lvl = lvl
		self.moves = moves
		self.hp = round(pokemon[4]/4) + 2 * lvl
		self.attack = round(pokemon[5]/9) + lvl
		self.deffence = round(pokemon[6]/9) + lvl
		self.sattack = round(pokemon[7]/9) + lvl
		self.sdeffence = round(pokemon[8]/9) + lvl
		self.speed = round(pokemon[9]/9) + lvl
