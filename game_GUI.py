import tkinter as tk
from tkinter import filedialog
from controller import GameController
import os

class GUI_2048():
	def __init__(self, controller):
		self.create_widgets()
		self.setController(controller)

	def __init__(self):
		self.create_widgets()
		self.setController(GameController())
		

	def create_widgets(self):
		self.game_window = tk.Tk(screenName="2048")
		self.new_game_button = tk.Button(self.game_window, text="NEW GAME",
									command = self.create_new_game)
		self.new_game_button.pack()
		self.save_button = tk.Button(self.game_window, text="SAVE GAME",
									command = self.save_game)
		self.save_button.pack()
		self.load_button = tk.Button(self.game_window, text="LOAD GAME",
									command = self.load_game)
		self.load_button.pack()
		self.game_board_area = GameBoardArea(self.game_window)
		self.game_board_area.pack()
		
		self.bind_keys()

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

	def startMainLoop(self):
		self.game_window.mainloop()

	def setController(self, controller):
		self.controller = controller
		self.game_board_area.updateGameBoard(self.controller.getCurrentGame().getGameBoard())

	#The functions talking to game window
	def create_new_game(self):
		self.controller.startNewGame()
		self.updateGameState()

	def save_game(self):
		filename = filedialog.asksaveasfilename(initialdir=os.getcwd()+"/game_saves")
		self.controller.saveGame(filename)

	def load_game(self):
		filename = filedialog.askopenfilename(initialdir=os.getcwd()+"/game_saves")
		self.controller.loadGame(filename)
		self.updateGameState()

	#The functions talking to game controller
	def updateGameState(self):
		self.game_board_area.updateGameBoard(self.controller.getCurrentGame().getGameBoard())
	
	def playGameStep(self, direction):
		if self.controller.playGameStep(direction):
			#Valid move
			self.updateGameState()




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
