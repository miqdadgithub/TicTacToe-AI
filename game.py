# import needed modules;
import time
from player import HumanPlayer, RandomComputerPlayer
import unbeatable_computer_player
# define game class;


class TicTacToe():
    def __init__(self):
        # define a board attribute for the game, which is a 3x3 list;
        # use underscore(_) as a variable in looping.
        self.board = [' ' for _ in range(9)]
# keeps track of current winner;
        self.current_winner = None
# define a function to print the board;

    def print_board(self):
        # using list comperhension to make a list of 3 elements, each is a list like [' ', ' ', ' '];
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # print separator, starts with| then for each row(^) in row (3spaces)spearate by | ends with |;
            print('|' + '|'.join(row) + '|')
# learn more about static methods;

    @staticmethod
    def print_board_nums():
        # again by list comperhension to a list of 3 lists, each is list like ['3j', '3j+1', '3j+2'];
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
# use the same logic as in the separator above(^);
        for row in number_board:
            print('|' + '|'.join(row) + '|')
# make a function to tell the available moves;

    def available_moves(self):
        # using list comperhension;
        # enumerate(list) is a list method that take a list and return a list of the elements tupled
        # with their Index e.g [1, '2', 3] -->[(0, 1), (1, '2'), (2, 3)]
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # which return a boolean if there is an empty squares or not.
        return ' ' in self.board

    def num_empty_squares(self):
        # which gives the number of empty squares.
        return len(self.available_moves())
        # another way deactivate above line to check!
        return self.board, count(' ')
# lets define a function to make a move;

    def make_move(self, square, letter):
        # if the move is valid we return true, otherwise return false.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
# lets define a function to fine the winner;

    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of the of these!
        # first check the row
        row_ind = square // 3  # divide by 3 and rounded down
        row = self.board[row_ind * 3: (row_ind + 1) * 3]  # get the row
        if all([spot == letter for spot in row]):  # which is true all row is same letter
            return True
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):  # which is true all column is same letter
            return True
        # check diagonals
        # to win a diagonal {0,2, 4, 6, 8} are the only moves
        if square % 2 == 0:
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all of these fail
        return False
# define a play function, return the winner(the letter) of the game! or None for a tie;


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'x'  # starting letter
# iterate while the game still have empty squares;
    while game.empty_squares():
        # get the moves from the appropriate player;
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
# let's define a function to make a move;
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('')  # just a empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter
# after we made our move, we need to alternate letters;
            letter = 'o' if letter == 'x' else 'x'
        # tiny break to make thing easier to read;
        time.sleep(1.2)
    if print_game:
        print('it\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = unbeatable_computer_player.GeniusComputerPlayer('o')
    game_t = TicTacToe()
    play(game_t, x_player, o_player, print_game=True)
