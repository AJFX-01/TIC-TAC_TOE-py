import random
import math

class Player():
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        pass



class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.symbol + '\'s turn. input move (0-8):')
            try:
                value = int(square)
                if value not in game.avaliable_moves():
                    raise(ValueError)
                valid_square = True
            except ValueError:
                print("INvalid Move, try again")
        return value

        
class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def get_move(self, game):
        square = random.choice(game.avaliable_moves())
        return square

class SuperPLayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        if len(game.avaliable_moves()) == 9:
            square = random.choice(game.avaliable_moves())
        else:
            square = self.minimax(game, self.symbol)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.symbol  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.no_empty_square() + 1) if other_player == max_player else -1 * (
                        state.no_empty_square() + 1)}
        elif not state.empty_square():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.avaliable_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best