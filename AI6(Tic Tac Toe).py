import random

board = ["-" , "-" , "-",
         "-" , "-" , "-",
         "-" , "-" , "-"]

currentPlayer = "X"
winner = None

gameRunning = True

#printing game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#take player input
def playerInput(board):
    inp = int(input("Enter number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Place already Taken!!!")

#Check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[0]
        return True

def checkRow(board):
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiag(board):
        print(f"The winner is {winner}")
        gameRunning = False


#Switch the player
def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

#Computer
def computer(board):
    while currentPlayer =="O":
        position = random.randint(0 , 8)
        if board[position] == "-":
            board[position] = "O"
            changePlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    printBoard(board)
    changePlayer()
    computer(board)
    checkWin()
    checkTie(board)