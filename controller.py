
from game_core import GameState
from data_manager import *
class GameController():
	def __init__(self, game):
		self.game = game
		self.dm_AI = None
		self.dm_game = GameDataManager()

	def __init__(self):
		self.game = GameState()
		self.dm_AI = None
		self.dm_game = GameDataManager()

	def startNewGame(self):
		self.game = GameState()


	def playGameStep(self, direction):
		if direction in self.game.available_moves():
			self.game = self.game.receive_command(direction)
			return True
		return False

	def getCurrentGame(self):
		return self.game

	def saveGame(self, path):
		self.dm_game.save_game(path, self.game)

	def loadGame(self, path):
		game_board = self.dm_game.load_game(path)
		self.game = GameState(board=game_board)