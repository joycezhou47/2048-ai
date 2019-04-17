import tkinter as tk
from controller import GameController

class GUI_2048():
	def __init__(self, controller):
		self.init_setup()
		self.setController(controller)

	def __init__(self):
		self.init_setup()
		self.setController(GameController())
		

	def init_setup(self):
		self.game_window = tk.Tk(screenName="2048")
		self.game_board_area = GameBoardArea(self.game_window)
		self.game_board_area.pack()
		self.bind_keys()


	def startMainLoop(self):
		self.game_window.mainloop()

	def setController(self, controller):
		self.controller = controller
		self.game_board_area.updateGameBoard(self.controller.getCurrentGame().getGameBoard())

	#The functions talking to game window
	def bind_keys(self):
		def leftKey(event):
			self.playGameStep("L")

		def rightKey(event):
			self.playGameStep("R")

		def upKey(event):
			self.playGameStep("U")

		def downKey(event):
			self.playGameStep("D")

		self.game_window.focus_set()
		self.game_window.bind("<Left>", leftKey)
		self.game_window.bind("<Right>", rightKey)
		self.game_window.bind("<Up>", upKey)
		self.game_window.bind("<Down>", downKey)


	#The functions talking to game controller

	def updateGameState(self, new_game_board):
		#TODO Only responsible for changing the game state area
		self.game_board_area.updateGameBoard(new_game_board)
	
	def playGameStep(self, direction):
		if self.controller.playGameStep(direction):
			#Valid move
			self.updateGameState(self.controller.getCurrentGame().getGameBoard())




class GameBoardArea(tk.Canvas):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.setGameSize(4)

	def setGameSize(self, size):
		self.game_size = size
		for l in self.grid_slaves():
			l.destroy()
		self.game_board_value = []
		for i in range(self.game_size):
			self.game_board_value.append([])
			for j in range(self.game_size):
				var = tk.StringVar()
				w = tk.Label(self, textvariable=var)
				w.grid(row=i, column=j)
				self.game_board_value[i].append(var)

	def updateGameBoard(self, board):
		if board.shape[0] != self.game_size:
			self.setGameSize(board.shape[0])
		for i in range(self.game_size):
			for j in range(self.game_size):
				self.game_board_value[i][j].set(str(board[i,j]))


if __name__ == "__main__":
	GUI = GUI_2048()
	GUI.startMainLoop()
