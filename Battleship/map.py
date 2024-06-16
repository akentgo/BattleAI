# So I want to paint the map itself, first I want to make a static array that is the map itself

class Map:
		def __init__(self):
			self.map_dim = [['a' for _ in range(5)] for _ in range(5)] #We have now made an array of 5x5 filled with 'a's
