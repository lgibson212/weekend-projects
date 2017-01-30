import random
import os
import time

print ('''
***********************************************
***********  Rock, Paper, Scissors  ***********
***********************************************
''')


class Player:
	def __init__(self, wins=0):
		self.name = input("Enter your name: ")
		self.wins = wins
		self.choice = None

	def make_choice(self):
		player_choice = input("{}, choose [1] rock, [2] paper or [3] scissors: ".format(self.name))
		if player_choice not in ['1', '2', '3']:
			print ('Invalid choice - please choose [1], [2], or [3]')
			time.sleep(1)
			self.make_choice()
		else:
			self.choice = player_choice


class Game:
	def __init__(self, target_score=3):
		self.players = []
		self.target_score = target_score
		self.winner = None
		self.winners = [] #list to store multiple winners, if more than one user hits the target_score
		self.round_count = 0
		self.add_player()
		self.round()

	def add_player(self):
		self.players.append(Player())
		self.add_more_players()
		return self.players

	def add_more_players(self):
		more_players = input("Will there be more players? [y or n] ")
		print ("\n")
		if more_players == "y":
			self.add_player()
		elif more_players == 'n':
			pass
		else:
			print('Not a valid input. Please type "y" or "n" on next try.')
			time.sleep(2)
			self.add_more_players()
		return self.players

	def round(self):
		self.round_count += 1
		os.system('clear')
		print("\n***********************************************")
		print("*******************  Round #{} *****************".format(self.round_count))
		print("***********************************************\n")

		for player in self.players:
			player.make_choice()
		self.compare()
		self.score_board()
		if self.check_wins():
			self.results()
		else:
			self.round()

	def random_computer_choice(self):
		rps = ['1', '2', '3']
		comp_choice = random.choice(rps)
		return comp_choice

	def compare(self):
		computer_choice = self.random_computer_choice()
		for player in self.players:
			if computer_choice == '1' and player.choice == '2':
				player.wins += 1
			elif computer_choice == '2' and player.choice == '3':
				player.wins += 1
			elif computer_choice == '3' and player.choice == '1':
				player.wins += 1

	def score_board(self):
		print ("\n")
		for player in self.players:
			print("{} has {} wins".format(player.name, player.wins))
		time.sleep(1)

	def check_wins(self):
		for player in self.players:
			if player.wins == self.target_score:
				self.winners.append(player.name)
		return self.winners

	def results(self):
		for winner in self.winners:
			print ('\n{} Wins!!'.format(winner))


g = Game()
#print (g.rand_comp_choice())
#guess = Guess()
#print (guess.player_choice())
# p = Player(self)
# p.name
