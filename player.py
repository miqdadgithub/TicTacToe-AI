# add all needed modules;
import math
import random
# create player class;


class Player():
    # will be initiated by either letter x or o;
    def __init__(self, letter):
        self.letter = letter
# define a function to give players their next move;

    def get_move(self, game):
        pass
# create a computer player based on player class;


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
# it returns a random empty Index on the board;

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
# create a human player based on player class;


class HumanPlayer(Player):
    def __init__(self, letter):
        self.letter = letter
# we want user to keep iterating till choosing a valid spot;

    def get_move(self, game):
        # the while loop we loop till find a valid square, and value of index is None;
        valid_square = False
        val = None
        while not(valid_square):
            square = input(self.letter + '\'s turn.Input move (0-8):')
# we'll use a try/except block to check if they enter a valid input;
            try:
                val = int(square)
                if val not in game.available_moves():
                    # raise an error;
                    raise ValueError
# if it get here it valid input;
                valid_square = True
            except ValueError:
                print('Invalid square, Try again.')
        return val
