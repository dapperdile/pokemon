class Pokemon_char:
	def __init__(self, dex_number=1, poke_type="Normal", lvl=1, moves=[]):
		self.dex_number = dex_number
		self.poke_type = poke_type
		self.lvl = lvl
		self.moves = moves
		self.attack = 49 + lvl * 2