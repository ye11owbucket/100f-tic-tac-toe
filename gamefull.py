from x01_data import *
from x02_display import *
from x03_winner import *

def tictact0e():
    board = [0,0,0,0,0,0,0,0,0]
    print("press b to see board")
    print('press i to place')

    while True:
        a = str(input('enter choice:'))
        if a == 'b':
            print(displayString(board))
        if a == 'i':
            square = input(str('enter position:'))
            player = input(str('enter X or O:'))
            write(player,board,square)
            return board
        
tictact0e()
    
