import math
import random


class Player():
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    # We want all players to get their next move given a game 
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square: # So when it will be false
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # We're going to checkl that this is a correct value by trying to cast
            # it to and integer, and if it's not, then we say its invalid
            # if that spot is not avaiblable on the board, we also say its invalid
            try:
                val = int(square) #square is the input user insert
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # *****When the computer will always win*****
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #Randomly choose one 
        else:
            # Get the square based off the minimax algorithm 
            square = self.minimax(game, self.letter)['position']
        return square

    # Algoritm 
    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X' #The other player.. so whatever letter is

        # first we want to check if the previous move is a winner
        # This is our base case
        if state.current_winner == other_player:
            #We should return position AND score becasue we need to keep track of the score 
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares(): #No empty squares 
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            # Step 1: Make a move, try that spot
            state.make_move(possible_move, player)
            # Step 2: Recurse using minimax to simulate agame after making that move 
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # Step 3: Undo the move 
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            # Step 4: Update the dictionaries if necessary 
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score #Replace best 
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score #Replace best
                    
        return best