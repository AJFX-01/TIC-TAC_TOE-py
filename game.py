from player import HumanPlayer, ComputerPlayer , SuperPLayer
import time
import math

class TicTac():
    def __init__(self):
        self.board = self.make_board() # 3x3 board
        self.current_winner = None # keep track of the winner

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        


    @staticmethod
    def print_no_board():
        # 0 | 1 | 2 what number correspond to the board
        no_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in no_board:
            print('| ' + ' | '.join(row) + ' |')

    def avaliable_moves(self):
        # return list of avaliable moves
        return [i for i, point in enumerate(self.board) if point == ' ']
        # for (i, point) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if point == ' ':
        #         moves.append(i)
        #     return moves
    def empty_square(self):
        return ' ' in self.board
    
    def no_empty_square(self):
        return self.board.count(' ')
    
    def make_move(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        
        return False
    
    def winner(self, square, symbol):
        # 3 symbol in a row shows the winner, be it vertical, diagonal, horizontal
        # check for rows(vertical)
        row_i = math.floor(square / 3)
        row = self.board[row_i*3 : (row_i + 1) *3]
        if all([point == symbol for point in row]):
            return True
        
        col_i = square % 3
        column = [self.board[col_i + i*3] for i in range(3)]
        if all(point == symbol for point in column):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(point == symbol for point in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(point == symbol for point in diagonal2):
                return True

        # if all checks fails then no winners
        return False
        

def play_game(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_no_board()

    symbol = 'x'
    while game.empty_square():
        if symbol == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, symbol):
            if print_game:
                print(symbol + ' make move to square {}'.format(square))
                game.print_board()
                print('')
        
            if game.current_winner:
                if print_game:
                    print(symbol + ' wins!')
                return symbol

            # Alternate moves
            symbol = 'o' if symbol == "x" else 'x'

        
        #time.sleep(.8)

    if print_game:
        print('it\'s a tie')

def main():
    xwins = 0
    owins = 0
    ties = 0
    for _ in range(50):
        x_player = SuperPLayer('x')
        o_player = ComputerPlayer('o')
        tic = TicTac()
        result = play_game(tic, x_player, o_player, print_game=True)
        if result == 'x':
            xwins += 1
        elif result == 'o':
            owins += 1
        else:
            ties +=1
        
    print(f"After 50 plays. we see {xwins} x wins and {owins} o wins. and {ties} ties")


if __name__ == "__main__":
    main()


