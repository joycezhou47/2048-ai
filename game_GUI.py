import tkinter as tk
from tkinter import filedialog
from controller import GameController
import os
import time

class GUI_2048():
	def __init__(self, controller):
		self.create_widgets()
		self.setController(controller)

	def __init__(self):
		self.create_widgets()
		self.setController(GameController())
		

	def create_widgets(self):
		self.game_window = tk.Tk(screenName="2048")
		new_game_button = tk.Button(self.game_window, text="NEW GAME",command = self.create_new_game)
		new_game_button.pack()

		save_button = tk.Button(self.game_window, text="SAVE GAME",command = self.save_game)
		save_button.pack()

		load_button = tk.Button(self.game_window, text="LOAD GAME", command = self.load_game)
		load_button.pack()

		self.AI_panel = AIPanel(self.game_window)
		self.AI_panel.setCommand("start_AI", self.start_AI)
		self.AI_panel.setCommand("stop_AI", self.stop_AI)

		#variable = tk.StringVar()
		#variable.set("one") # default value
		#w = tk.OptionMenu(self.game_window, variable, "one", "two", "three")
		#w.pack()
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

		def onWindowClose():
			self.controller.endGame()
			self.game_window.destroy()

		self.game_window.focus_set()
		self.game_window.bind("<Left>", leftKey)
		self.game_window.bind("<Right>", rightKey)
		self.game_window.bind("<Up>", upKey)
		self.game_window.bind("<Down>", downKey)
		self.game_window.protocol("WM_DELETE_WINDOW", onWindowClose)

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

	def load_AI(self, AI_name):
		#TODO
		pass

	def start_AI(self):
		self.controller.setAIMoving(True)
		self.move_AI()

	def stop_AI(self):
		self.controller.setAIMoving(False)

	def move_AI(self):
		if not self.controller.isAIMoving():
			return
		self.playGameStep(self.controller.getAIMove())
		self.game_window.after(500, self.move_AI)


class AIPanel(tk.Canvas):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):

		AI_start_button = tk.Button(self, name="start_AI", text="AI PLAY")
		AI_start_button.pack()

		AI_stop_button = tk.Button(self, name="stop_AI", text="AI STOP")
		AI_stop_button.pack()

	def setCommand(self, method_name, method):
		self.children[method_name].configure(command=method)

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
