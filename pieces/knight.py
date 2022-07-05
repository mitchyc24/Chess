import os
import pygame as pg


class Knight:
    
    IMG_B = pg.image.load(os.path.join("assets","bn.png"))
    IMG_W = pg.image.load(os.path.join("assets","wn.png"))

    def __init__(self, colour):
        self.colour = colour
        
    @property
    def FEN_letter(self):
        if self.colour == "white": return "N"
        if self.colour == "black": return "n"