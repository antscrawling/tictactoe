import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def check_spot(self,row,col):
        if row > 3 or col > 3:
            print('Try again')
            return False
        else:
            if self.board[row][col] == 'O' or self.board[row][col] == 'X':
                print('That spot is taken')
                print(self.board)
                return False
        return True

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        #for row in self.board:
        #    for item in row:
        #        if item == '-':
        #            return False
        #return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player,x,y):
        if not self.check_spot(x,y) and x>y:
            return 'X'
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        countO = 0
        countX = 0
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            if player  == 'X':
                print(f"Player {player} turn, no {str(countX+1)}")
            else : print(f"Player {player} turn, no {str(countO+1)}")
            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
            try:
                if self.check_spot(row -1,col-1):

            # fixing the spot
                    self.fix_spot(row - 1, col - 1, player)
                    if player =='O':countO +=1
                    if player == 'X':countX +=1
                    player = self.swap_player_turn(player,countO,countX)
            except: continue


            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
