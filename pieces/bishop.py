import os
import pygame as pg


class Bishop:
    
    IMG_B = pg.image.load(os.path.join("assets","bb.png"))
    IMG_W = pg.image.load(os.path.join("assets","wb.png"))

    def __init__(self, colour):
        self.colour = colour


    @property
    def FEN_letter(self):
        if self.colour == "white": return "B"
        if self.colour == "black": return "b"