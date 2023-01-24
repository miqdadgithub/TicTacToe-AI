# import all needed modules;
from player import *
import random
import math
# let define a unbeatable player class  that uses minimax algorithms;


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # pick a corner will ensure a win or tie;
            square = random.choice([0, 2, 6, 8])
            # square = random.choice(game.available_moves())#pick a random one
        else:
            # get square based on minimax algorithms;
            square = self.minimax(game, self.letter)['position']
        return square
# define the minimax function;

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if player == 'x'else 'x'
# first we check if the previous move was a winner
        if state.current_winner == other_player:
            # we return postion and score because we need to keep track of score for mini max to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1
                    )
                    }
        elif not(state.empty_squares()):  # no empty squares
            return {'position': None, 'score': 0}
        if player == max_player:
            # each score should maximize
            best = {'position': None, 'score': -math.inf}
        else:
            # each score should minimize
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1:make a move, try that spot
            state.make_move(possible_move, player)
            # step 2:recurse using minimax to simulate a game after making that move
            # now we alternate players
            sim_score = self.minimax(state, other_player)
            # step 3:undo that move
            state.board[possible_move] = ' '
            state.current_winner = None
            # otherwise this will get messed up from the recursion
            sim_score['position'] = possible_move
            # step 4:update the dictionaries if necessary
            if player == max_player:  # maximizing max_player
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:  # minimixing the other_player
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best

        return best
