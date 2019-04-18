
from game_core import GameState
from data_manager import *
from game_AI import PLAYER2048
class GameController():
	def __init__(self, game):
		self.game = game
		self.AI = PLAYER2048.getPlayer("Randmie", game_size=self.game.game_size)
		self.dm_game = GameDataManager()
		self.AImoving = False
		self.cur_game_path = None

	def __init__(self):
		self.game = GameState()
		self.AI = PLAYER2048.getPlayer("Randmie", game_size=self.game.game_size)
		self.dm_game = GameDataManager()
		self.AImoving = False
		self.cur_game_path = None

	def startNewGame(self):
		self.game = GameState()

	def playGameStep(self, direction):
		if direction in self.game.available_moves():
			if not self.AImoving:
				#Currently a human is taking control, let's teach our AI
				self.AI.take_data(self.game, direction)
			self.game = self.game.receive_command(direction)
			return True
		return False

	def getCurrentGame(self):
		return self.game

	def curGameFinished(self):
		return self.game.game_ended()

	def saveGame(self, path):
		self.cur_game_path = path
		self.dm_game.save_game(path, self.game)

	def loadGame(self, path):
		self.cur_game_path = path
		game_board, score = self.dm_game.load_game(path)
		self.game = GameState(board=game_board, score=score)
		self.setAIMoving(False)

	def endGame(self):
		if self.cur_game_path:
			self.dm_game.save_game(self.cur_game_path, self.game)
		self.AI.end_training()

	def loadAI(self, AI_name):
		self.AI = PLAYER2048.getPlayer(AI_name, game_size=self.game.game_size)

	def getAIMove(self):
		return self.AI.respond(self.game)

	def setAIMoving(self, AImoving):
		self.AImoving = AImoving

	def isAIMoving(self):
		return self.AImoving