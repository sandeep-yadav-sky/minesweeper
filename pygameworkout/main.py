from game1 import Game
from board import Board
size = (9,9)
prob = 0.1
board = Board(size,prob)
screenSize = (800, 800)

game = Game(board, screenSize)
game.run()