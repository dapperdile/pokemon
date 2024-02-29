class Pokemon_char:
	def __init__(self, pokemon, lvl=1, moves=[]):
		self.name = pokemon[1]
		self.poke_type = pokemon[2]
		self.poke_type2 = pokemon[3]
		self.lvl = lvl
		self.moves = moves
		self.hp = pokemon[4]
		self.attack = pokemon[5]
		self.deffence = pokemon[6]
		self.sattack = pokemon[7]
		self.sdeffence = pokemon[8]
		self.speed = pokemon[9]