'''This project is made by musab schluck and it's goal is to give a table of approximated probabilities
to playing the Roulette game assuming a player is:
	- playing in a table that has one zero tile European style
	- playing continusly until he loses all of his money or reached the desired
	- playing on the odd and even mode, in which if the outcome is even and the player choose an even outcoome he'll get 10$
	- winning a 10$ or losing 10$ at each game
'''
import numpy as np
import pandas as pd
from random import choice

class Player:
	def __init__(self, money, desired_amount):
		self.money = money
		self.desired_amount = desired_amount
		self.num_of_games_played = 0
		self.num_of_times_won = 0
		self.odd_or_even = choice(["odd", 'even'])
		self.stop_playing = False

	def decide_to_quit_or_continue_playing(self):
		if self.money == self.desired_amount or self.money == 0:
			self.stop_playing = True



class Table:
	def __init__(self, num_of_zeros):
		# num of zeros = 0 to demonstrate the effect, one zero in european cpuntries, two zerso in America
		# if 0 the casino wins
		# if odd number and the player picked odd, the player win and vise versa
		if num_of_zeros == 0:
			self.nums = range(1, 37)
		elif num_of_zeros == 1:
			self.nums = range(37)
		elif num_of_zeros == 2:
			self.nums = list(range(37))
			self.nums.append(0)

	def spin(self, player):
		outcome = choice(self.nums)
		if outcome == 0:
			player.money -= 10
		elif player.odd_or_even == "even" and outcome%2 == 0:
			player.money += 10
			player.num_of_times_won += 1
		elif player.odd_or_even == "odd" and outcome%2 != 0:
			player.money += 10
			player.num_of_times_won += 1
		else:
			player.money -= 10

		player.num_of_games_played += 1

init_money = 100
desired_amount = 200
num_of_iterations = 100
num_of_zeros = 0
data = {
	"number of zeros": [],
	"initial money": [],
	"desired money": [],
	"avg num of games played": [],
	"avg winning ratio": []
}


for init_money in range(100, 1000, 100):		#range(100, 1100, 100):
	for desired_amount in range(init_money, init_money+210, 10):
		for i in range(num_of_iterations):
			p, t = Player(init_money, desired_amount), Table(num_of_zeros = num_of_zeros)
			while not p.stop_playing:
				t.spin(p)
				p.decide_to_quit_or_continue_playing()
		data["number of zeros"].append(num_of_zeros)
		data["initial money"].append(init_money)
		data["desired money"].append(desired_amount)
		data["avg num of games played"].append(p.num_of_games_played)
		data["avg winning ratio"].append((p.num_of_times_won/p.num_of_games_played)*100)
d = pd.DataFrame(data)
print(d)



# init money	desired money	avg num of games played 	avg winning ratio
#    100        110, 120,..300													table 1
#	 200		210, 220,..400													table 2
#	.....
#	1000		1010.....1200													table 10

