import os
import pygame as pg


class Pawn:
    
    IMG_B = pg.image.load(os.path.join("assets","bp.png"))
    IMG_W = pg.image.load(os.path.join("assets","wp.png"))

    def __init__(self, colour):
        self.colour = colour

    @property
    def FEN_letter(self):
        if self.colour == "white": return "P"
        if self.colour == "black": return "p"