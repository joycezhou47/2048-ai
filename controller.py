
from game_core import GameState
from data_manager import *
from game_AI import PLAYER2048
class GameController():
	def __init__(self, game):
		self.game = game
		self.AI = PLAYER2048.getPlayer("Randmie", game_size=self.game.game_size)
		self.dm_game = GameDataManager()
		self.AImoving = False

	def __init__(self):
		self.game = GameState()
		self.AI = PLAYER2048.getPlayer("Randmie", game_size=self.game.game_size)
		self.dm_game = GameDataManager()
		self.AImoving = False

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

	def getAIMove(self):
		return self.AI.respond(self.game)

	def setAIMoving(self, AImoving):
		self.AImoving = AImoving

	def isAIMoving(self):
		return self.AImoving