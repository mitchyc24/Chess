'''
Chess Engine
Written by Mitchell Carroll
05 July 2022
'''

import numpy as np

from pieces.knight import Knight
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King




class Chess_Engine:
    '''
    Chess_Engine class is responsible for game logic
    '''
    def __init__(self) -> None:
        self.move_log = []
        self.current_turn = 0 #0 for white, 1 for black
        self.current_board = np.array([
        [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
        [Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white")],
        [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ])


    

    def get_current_FEN(self):
        return "r2qk3/p1pp1p1p/5n2/1B6/3bbQ2/2P2R2/PP5P/RNB3rK w q - 1 16"