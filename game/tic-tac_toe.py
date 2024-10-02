import random

# Constants for player types
COMPUTER = 1
HUMAN = 2

# Length of the board
SIDE = 3

# Symbols for computer and human
COMPUTERMOVE = 'O'
HUMANMOVE = 'X'


# Function to show the current board status
def showBoard(board):
    print("\n\n")
    print("\t\t\t", board[0][0], "|", board[0][1], "|", board[0][2])
    print("\t\t\t--------------")
    print("\t\t\t", board[1][0], "|", board[1][1], "|", board[1][2])
    print("\t\t\t--------------")
    print("\t\t\t", board[2][0], "|", board[2][1], "|", board[2][2])
    print("\n")


# Function to show the instructions
def showInstructions():
    print("\t\t\t Tic-Tac-Toe\n\n")
    print("Choose a cell numbered from 1 to 9 as below and play\n\n")
    print("\t\t\t 1 | 2 | 3 ")
    print("\t\t\t--------------")
    print("\t\t\t 4 | 5 | 6 ")
    print("\t\t\t--------------")
    print("\t\t\t 7 | 8 | 9 \n")
    print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n\n")


# Function to initialise the game
def initialise(board):
    # Initially the board is empty
    for i in range(SIDE):
        for j in range(SIDE):
            board[i][j] = ' '


# Function to declare the winner of the game
def declareWinner(whoseTurn):
    if whoseTurn == COMPUTER:
        print("COMPUTER has won\n")
    else:
        print("HUMAN has won\n")


# Function to check if any row is crossed
def rowCrossed(board):
    for i in range(SIDE):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return True
    return False


# Function to check if any column is crossed
def columnCrossed(board):
    for i in range(SIDE):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True
    return False


# Function to check if any diagonal is crossed
def diagonalCrossed(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False


# Function to check if the game is over
def gameOver(board):
    return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)


# Function to play Tic-Tac-Toe
def playTicTacToe(whoseTurn):
    # A 3x3 Tic-Tac-Toe board for playing
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    availableMoves = list(range(1, SIDE * SIDE + 1))

    # Initialise the game
    initialise(board)

    # Show the instructions before playing
    showInstructions()

    moveIndex = 0

    # Keep playing till the game is over or it's a draw
    while not gameOver(board) and moveIndex != SIDE * SIDE:
        if whoseTurn == COMPUTER:
            move = random.choice(availableMoves)  # Computer randomly chooses a move
            availableMoves.remove(move)

            x = (move - 1) // SIDE
            y = (move - 1) % SIDE
            board[x][y] = COMPUTERMOVE
            print(f"COMPUTER has put a {COMPUTERMOVE} in cell {move}")
            showBoard(board)
            whoseTurn = HUMAN

        elif whoseTurn == HUMAN:
            while True:
                try:
                    move = int(input("Enter your move (1-9): "))
                    if move in availableMoves:
                        availableMoves.remove(move)
                        break
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a valid number between 1 and 9.")

            x = (move - 1) // SIDE
            y = (move - 1) % SIDE
            board[x][y] = HUMANMOVE
            print(f"HUMAN has put a {HUMANMOVE} in cell {move}")
            showBoard(board)
            whoseTurn = COMPUTER

        moveIndex += 1

    # If the game is a draw
    if not gameOver(board) and moveIndex == SIDE * SIDE:
        print("It's a draw\n")
    else:
        # Declare the winner
        if whoseTurn == COMPUTER:
            whoseTurn = HUMAN
        else:
            whoseTurn = COMPUTER

        declareWinner(whoseTurn)


# Driver program
if __name__ == '__main__':
    # Play the game with COMPUTER starting first
    playTicTacToe(HUMAN)
