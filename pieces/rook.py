import os
import pygame as pg


class Rook:
    
    IMG_B = pg.image.load(os.path.join("assets","br.png"))
    IMG_W = pg.image.load(os.path.join("assets","wr.png"))

    def __init__(self, colour):
        self.colour = colour

    @property
    def FEN_letter(self):
        if self.colour == "white": return "R"
        if self.colour == "black": return "r"