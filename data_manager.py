import numpy as np 
import os.path

AI_PATH = "AI_datas"
GAME_PATH = "game_saves"

class AIDataManager():
	def __init__(self, AI_name="default",  game_size=4):
		self.AI_name = AI_name
		self.file_name = AI_name + "." + str(game_size) + ".npz"
		self.file_full_path = AI_PATH + "/" + self.file_name
		self.X = np.array([])
		self.y = np.array([])
		if not os.path.exists(self.file_full_path):
			self.save_data() #Create an empty record
		#self.load_data()

	def load_data(self):
		with np.load(self.file_full_path) as f:
			self.X = f["X"]
			self.y = f["y"]

	def save_data(self):
		np.savez(self.file_full_path, X=self.X, y=self.y)

	def append_new_data(self, new_X, new_y):
		self.X = np.concatenate(self.X, new_X)
		self.y = np.concatenate(self.y, new_y)

	def end_session(self):
		self.save_data()

class GameDataManager():
	def load_game(self, path):
		return np.load(path)['game_state']

	def save_game(self, path, game):
		np.savez(path, game_state=game.board)
