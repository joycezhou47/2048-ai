from game_core import *

game = GameState()

while(not game.game_ended()):
	print(game.text_interface())
	available_moves = game.available_moves()
	command = input("Enter next move {} :".format(available_moves))
	while command not in available_moves:
		command = input("Enter next move {} :".format(available_moves))
	game = game.receive_command(command)
