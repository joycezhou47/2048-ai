
from game_core import GameState
class GameController():
	def __init__(self, game):
		self.game = game

	def __init__(self):
		self.game = GameState()


	def playGameStep(self, direction):
		if direction in self.game.available_moves():
			self.game = self.game.receive_command(direction)
			return True
		return False

	def getCurrentGame(self):
		return self.game