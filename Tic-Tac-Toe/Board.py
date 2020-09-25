# board = [" " for x in range(10)]

def insertLetter(board, letter, pos):
    board[pos] = letter

def spaceIsFree(board, pos):
    return board[pos] == " "

def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def isWinner(board, letter):

    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter))


def playerMove(board, letter):
    boardBenchmark = board.count(" ")
    hasMoved = board.count(" ")
    while boardBenchmark == hasMoved:
        playerInput = input("Select a position 1 - 9: \n")
        try:
            pos = int(playerInput)
            if 0 < pos < 10:
                if spaceIsFree(board, pos):
                    insertLetter(board, letter, pos)
                    hasMoved = board.count(" ")
                else:
                    print("Please choose and empty position:")
                    printBoard(board)
            else:
                print("Please choose a position between 1 and 9.")
        except ValueError:
            print("Please enter an integer between 1 and 9.")


def computerMove(board, letter):
    possibleMoves = [x for x, letter, in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["o", "x"]:
        print("I'm in the top for-branch in computer move.")
        for i in possibleMoves:
            print("I'm in the nested for-branch in computer move.")
            print(f"These are my possible moves: {i}")
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                print("I'm in the if-branch of the nested for-branch.")
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move



def selectRandom(listofMoves):
    import random
    ln = len(listofMoves)
    r = random.randrange(0,ln)
    return listofMoves[r]

def assignLetter():
    from random import choice
    letters = ["x", "o"]
    computer = choice(letters)

    if computer == "x":
        player = "o"
    else:
        player = "x"

    return computer, player





def main():
    board = [" " for x in range(10)]

    computer, player = assignLetter()

    print(f"Computer is '{computer}' and player is '{player}'")

    print("Welcome to tic-tac-toe.")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board,computer)):
            playerMove(board, player)
            printBoard(board)
        else:
            print("Sorry you lose...")
            break

        if not(isWinner(board, player)):
            move = computerMove(board, computer)
            if move == 0:
                print("Tie game.")
            else:
                insertLetter(board, computer, move)
                print(f"Computer placed an {computer} on position {move}.")
                printBoard(board)
        else:
            print("You win!")
            break

        if isBoardFull(board):
            print("Tie game.")










