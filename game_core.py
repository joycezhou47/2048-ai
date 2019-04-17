import numpy as np

GAME_SIZE = 4
NEW_NUMBER_PROB = [0.8, 0.2]

class GameState():
	def __init__(self, game_size=GAME_SIZE, board=None):
		if board is not None:
			self.board = board
			self.game_size = board.shape[0]
		else: 
			self.board = np.zeros((game_size, game_size),dtype=np.int32)
			self.game_size = game_size
			#Drop 2 numbers at beginning
			self.drop_number_at_random()
			self.drop_number_at_random()


	def drop_number_at_random(self, new_numnber=2):
		empty_place_x, empty_place_y = np.where(self.board==0)
		i = np.random.randint(len(empty_place_x))
		self.board[empty_place_x[i], empty_place_y[i]] = new_numnber

	def shift_to_left(self):
		for i in range(self.game_size):
			j = 0
			for k in range(self.game_size):
				if self.board[i,k] != 0:
					#potential swap position 
					self.board[i, j], self.board[i, k] = self.board[i, k], self.board[i, j]
					j += 1

	def merge_towards_left(self):
		for i in range(self.game_size):
			for j in range(self.game_size-1):
				if self.board[i, j] == self.board[i,j+1]:
					self.board[i,j]*=2
					self.board[i,j+1] = 0
		self.shift_to_left()

	def receive_command(self,command):
		#Possible command: U, D, R, L
		other = GameState(board=self.board)
		if command == "L":
			other.shift_to_left()
			other.merge_towards_left()
		if command == "R":
			other.board = np.flip(other.board, 1)
			other.shift_to_left()
			other.merge_towards_left()
			other.board = np.flip(other.board, 1)
		if command == "U":
			other.board = np.flip(other.board.T, 0)
			other.shift_to_left()
			other.merge_towards_left()
			other.board = np.flip(other.board, 0).T	
		if command == "D":
			other.board = np.flip(other.board.T,1)
			other.shift_to_left()
			other.merge_towards_left()
			other.board = np.flip(other.board, 1).T
		other.drop_number_at_random()
		return other

	def game_ended(self):
		return len(self.available_moves()) == 0

	def available_moves(self):
		available_moves = set()
		board = self.board
		for i in range(self.game_size):
			for j in range(self.game_size - 1):
				#Empty space on board
				if board[i,j] == 0 and board[i,j+1] != 0:
					available_moves.add("L")
				if board[i,4-j-1] == 0 and board[i,4-j-2] != 0:
					available_moves.add("R")
				if board[j,i] == 0 and board[j+1,i] != 0:
					available_moves.add("U")
				if board[4-j-1,i] == 0 and board[4-j-2,i] != 0:
					available_moves.add("D")
				if board[i,j] != 0 and board[i,j] == board[i,j+1]:
						available_moves.add("R")
						available_moves.add("L")
				if board[j,i] != 0 and board[j,i] == board[j+1,i]:
						available_moves.add("D")
						available_moves.add("U")	
		return available_moves					

	def getGameBoard(self):
		return self.board

'''
	illy designed functions
	def valid_command(self, command):
		return command in self.available_moves()

	def text_interface(self):
		return str(self.board)
'''