from PIL import Image
import pygame as pg
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


class Board:
    '''
    Board class is reponsible for all things visual on the board. 
    '''

    piece_img_dict = {"p":Pawn.IMG_B, "r":Rook.IMG_B, "n":Knight.IMG_B, "b":Bishop.IMG_B, "q":Queen.IMG_B, "k":King.IMG_B,
        "P":Pawn.IMG_W, "R":Rook.IMG_W, "N":Knight.IMG_W, "B":Bishop.IMG_W, "Q":Queen.IMG_W, "K":King.IMG_W}

    def __init__(self, settings) -> None:
        self.settings = settings
        self.empty_board = self._create_board_image()
        self.FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    @property
    def surface(self):
        surface = pg.Surface(self.empty_board.get_size())

        #Board
        surface.blit(self.empty_board, (0,0))

        #Pieces
        splits = self.FEN.split()
        rows = splits[0].split("/")
        for i, row in enumerate(rows):
            offset = 0 
            for j, c in enumerate(row):
                if c.isdecimal(): offset += int(c)-1
                if c in self.piece_img_dict:
                    pixel_pos = self._get_pixel_position((j+offset,i))
                    img = self.piece_img_dict[c]
                    size = tuple(map(lambda x:x//8, self.settings["board_size"]))
                    img = pg.transform.smoothscale(img, size)
                    surface.blit(img, pixel_pos)
        return surface


    def set_FEN(self, fen):
        self.FEN = fen

    def _get_pixel_position(self, xy):
        x, y = xy
        dx, dy = self.empty_board.get_size()
        dx //= 8
        dy //= 8
        return (dx*x, dy*y)  

    def _create_board_image(self):
        def helper_get_square_pixels(row,col,size):
            col_start = int(size/8 * col)
            col_end = int(col_start + size/8)
            row_start = int(size/8 * row)
            row_end = int(row_start + size/8)
            pixels = []
            for row in range(row_start,row_end):
                for col in range(col_start,col_end):
                    pixels.append((row,col))
            return pixels

        img = Image.new("RGB", self.settings["board_size"], color=tuple(self.settings["board_black_colour"]))
        pixels = img.load()
        for square in range(64):
            row = square // 8
            col = square % 8
            if (row + col) % 2 == 0:
                sp = helper_get_square_pixels(row,col,self.settings["board_size"][0])
                for pixel in sp:
                    x,y = pixel
                    pixels[x,y] = tuple(self.settings["board_white_colour"])
        return pg.image.fromstring(img.tobytes(), img.size, img.mode)

    def convert_board_pixels_to_pos(self, board_pixel_xy):
        x_pixel, y_pixel = board_pixel_xy
        total_x_pixels, total_y_pixels = self.empty_board.get_size()
        pos = (int(x_pixel/total_x_pixels*8), int(y_pixel/total_y_pixels*8))
        print(pos)
        return pos
