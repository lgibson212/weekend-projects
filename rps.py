import random

class Player:
	def __init__(self, wins=0):
		self.name = input("Enter your name: ")
		self.wins = wins
		self.choice = None

	def make_choice(self):
		player_choice = input("{}, choose [1] rock, [2] paper or [3] scissors: ".format(self.name))
		if player_choice not in ['1', '2', '3']:
			print ('Invalid choice - please choose again')
			self.make_choice()
		else:
			self.choice = player_choice


class Game:
	def __init__(self, target_score=5):
		self.players = []
		self.target_score = target_score
		self.winner = None
		self.add_player()
		self.round()

	def add_player(self):
		self.players.append(Player())
		more_players = input("Will there be more players? [y or n]")
		#need to validate yes or no
		if more_players == "y":
			self.add_player()
		return self.players

	def round(self):
		for player in self.players:
			player.make_choice()
		self.compare()
		if self.check_wins():
			self.results()
		else:
			self.round()

	def rand_comp_choice(self):
		rps = ['1', '2', '3']
		comp_choice = random.choice(rps)
		return comp_choice

	def compare(self):
		comp_choice = self.rand_comp_choice()
		for player in self.players:
			if comp_choice == '1' and player.choice == '2':
				player.wins += 1
			elif comp_choice == '2' and player.choice == '3':
				player.wins += 1
			elif comp_choice == '3' and player.choice == '1':
				player.wins += 1

	def check_wins(self):
		for player in self.players:
			#How to deal with multiple players scoring 5
			if player.wins == self.target_score:
				self.winner == player
				return True
			else:
				return False

	def results(self):
		print ('{} Wins!!'.format(player.name))


#
g = Game()
#print (g.rand_comp_choice())
#guess = Guess()
#print (guess.player_choice())
# p = Player(self)
# p.name



