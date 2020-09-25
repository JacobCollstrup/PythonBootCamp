from Board import insertLetter
from Board import spaceIsFree
from Board import printBoard
from Board import isBoardFull
from Board import isWinner
from Board import playerMove
from Board import computerMove
from Board import selectRandom
from Board import assignLetter
from Board import main
"""
board = [" " for x in range(10)]
print(board)

insertLetter(board, "o", 1)
insertLetter(board, "o", 5)
insertLetter(board, "o", 9)

printBoard(board)

print(isBoardFull(board))

print(isWinner(board, "x"))

"""

while True:
    x = input("Would you like to play again? (y/n)")
    if x.lower() == "y":
        main()
    else:
        break