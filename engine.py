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
        self.current_turn = "w"
        self.castling = "KQkq"
        self.en_passant = "-"
        self.halfmove_clock = 0
        self.fullmoves = 1
        self.current_board = np.array([
        [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
        [Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white"),Pawn("white")],
        [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ])


    

    def get_current_FEN(self):
        piece_str = ""
        for i, row in enumerate(self.current_board):
            space_count = 0
            for j, square in enumerate(row):
                if square:
                    if space_count:
                        piece_str += str(space_count)
                        space_count = 0
                    piece_str += square.FEN_letter
                else:
                    if j==7:
                        piece_str += str(space_count)
                    else:
                        space_count += 1

            if i != 7:    
                piece_str += "/"

        fen = " ".join([piece_str, self.current_turn, self.castling, str(self.en_passant), str(self.halfmove_clock), str(self.fullmoves)])  
        print(fen) 
        return fen