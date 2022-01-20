from x01_data import *
from x02_display import *
from x03_winner import *
from test import *

def tictact0e():
    board = [0,0,0,0,0,0,0,0,0]
    print("press b to see board")
    print('press i to place')

    while True:
        a = str(input('enter choice:'))
        if a == 'b':
            print(displayString(board))
        if a == 'i':
            square = input('enter position:')
            player = input(str('enter X or O:'))
            write(square,board,player) 
            return board
        
print(tictact0e())
    
