import os
import pygame as pg


class Queen:
    
    IMG_B = pg.image.load(os.path.join("assets","bq.png"))
    IMG_W = pg.image.load(os.path.join("assets","wq.png"))

    def __init__(self, colour):
        self.colour = colour


    @property
    def FEN_letter(self):
        if self.colour == "white": return "Q"
        if self.colour == "black": return "q"