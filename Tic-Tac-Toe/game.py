
import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None #Keep track of winner!

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        # This is just geting the rows 
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (Tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if valid move, then the move (assign square to letter)
        # Then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True

        # Check colum    
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        
        # Check diagonals 
        # But only if the square is an even number (0, 2, 4, 6, 8)
        # These are the only moves possible to win a diagonal
        if square % 2 == 0: #if the square is even
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #Left to right diagonal
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # Right to left diagonal 
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        # if all of these fail 
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X' # Starting letter 
    # iterate while the game still has empty squares 
    # (We don't have to worry about winner becasue we'll just return that which brakes the loop )
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Let's define a function to make a move!    
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') # Just an empty line 

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            # After we made our move, we need to alernate letters    
            letter = 'O' if letter == 'X' else 'X'  # switches player
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        #Tiny break to make things a little easier to read 
        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



# if __name__ == '__main__':
#     x_player = SmartComputerPlayer('X')
#     o_player = HumanPlayer('O')
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game=True)

if __name__ == '__main__':
    x_win = 0
    o_win = 0
    ties = 0
    for _ in range(10):
        x_player = RandomComputerPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_win += 1
        elif result == '0':
            o_wins += 1
        else:
            ties += 1
    print(f'after 1000 ireration, we see {x_win} x wins, {o_win} o wins, and {ties} ties')

