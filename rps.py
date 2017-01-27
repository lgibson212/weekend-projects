class Player:
	def __init__(self, name, wins=0):
		self.name = name
		self.wins = wins
		#changes


class Guess:
	def __init__(self, choice):
		self.choice = choice

	def player_choice(self):
		pass


class Game:
	def __init__(self):
		self.players = []
		self.score

	def add_player(self):
		name = input("Enter your name: ")
		player = Player(name)
		self.players.append(player)
		return self.players

	def rand_comp_choice(self):
		pass

	def compare(self):
		pass

	def results(self):



