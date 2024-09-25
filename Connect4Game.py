class Connect4():
    def __init__(self):
        self.numberOfColumns = 7
        self.numberOfLines = 6
        self.board = [ ['  ' for _ in range(self.numberOfColumns)] for _ in range(self.numberOfLines) ]
    
    def displayBoard(self):
        for line in self.board:
            print("_" * self.numberOfColumns * 4)
            print(*line, sep=' |')
        print('    '.join(str(x) for x in range(self.numberOfColumns)))
    
    def isAvailable(self, line, column):
        return line[column] == '  '

    def player_choice(self):
        choice = int(input("Please select a column between 0 and 6: "))
        while choice < 0 or choice > 6 or self.board[0][choice] != '  ':
            choice = int(input("Invalid column or full. Please choose again between 0 and 6: "))
        return choice

    def player_input(self):
        player1 = input("Player 1, choose 'X' or 'O': ").upper()
        while player1 not in ['X', 'O']:
            player1 = input("Invalid choice! Please pick 'X' or 'O': ").upper()
        player2 = 'O' if player1 == 'X' else 'X'
        print(f"Player 1 is {player1}, Player 2 is {player2}")
        return player1, player2

    def checkLines(self, marker, board=None):
        if board is None:
            board = self.board
        # Check rows
        for line in board:
            for i in range(len(line) - 3):
                if line[i] == line[i+1] == line[i+2] == line[i+3] == " " + marker:
                    return True
        return False

    def checkDiags(self, marker):
        # Check diagonals
        for row in range(self.numberOfLines - 3):
            for col in range(self.numberOfColumns - 3):
                if self.board[row][col] == " " + marker and self.board[row+1][col+1] == " " + marker \
                   and self.board[row+2][col+2] == " " + marker and self.board[row+3][col+3] == " " + marker:
                    return True
                if self.board[row+3][col] == " " + marker and self.board[row+2][col+1] == " " + marker \
                   and self.board[row+1][col+2] == " " + marker and self.board[row][col+3] == " " + marker:
                    return True
        return False

    def generateReversedBoard(self):
        reversedBoard = [list(column) for column in zip(*self.board)]
        return reversedBoard

    def play(self, playercolumn, marker):
        for item in reversed(self.board):
            if self.isAvailable(item, playercolumn):
                item[playercolumn] = " " + marker
                return True
        return False

# Main game function
def play_game():
    game = True
    while game:
        c = Connect4()
        player1, player2 = c.player_input()
        currentPlayer = player1
        win = False

        while not win:
            c.displayBoard()
            print(f"{currentPlayer}'s turn")
            col_choice = c.player_choice()
            c.play(col_choice, currentPlayer)

            # Check for win or draw
            reversedBoard = c.generateReversedBoard()
            if c.checkLines(currentPlayer) or c.checkLines(currentPlayer, reversedBoard) or c.checkDiags(currentPlayer):
                win = True
                c.displayBoard()
                print(f"Game won by {currentPlayer}!")
                break

            # Switch player
            currentPlayer = player2 if currentPlayer == player1 else player1

        replay = input("Do you want to play again (Y/N)? ").lower()
        if replay == 'n':
            game = False
            print("Game ended!")

play_game()
