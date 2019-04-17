from data_manager import AIDataManager
from abc import ABC, abstractmethod
import numpy as np

special_AI = ["Randmie", "LogicRightie"]

class PLAYER2048():
	def getPlayer(p_name, game_size=4):
		if p_name not in special_AI:
			return AI2048(AI_name, game_size)
		if p_name == "Randmie":
			return Random2048()

	@abstractmethod
	def respond(self, cur_board):
		pass

	def endTraining(self):
		return


class AI2048(PLAYER2048):
	def __init__(self, AI_name, game_size=4):
		self.AI_name = AI_name
		self.DM = AIDataManager(AI_name, game_size)

	def respond(self, cur_game_state):
		pass

	def endTraining(self):
		self.DM.end_session()

class Random2048(PLAYER2048):
	def respond(self, cur_game_state):
		return np.random.choice(list(cur_game_state.available_moves()))


