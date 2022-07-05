import os
import pygame as pg


class Knight:
    
    IMG_B = pg.image.load(os.path.join("assets","bn.png"))
    IMG_W = pg.image.load(os.path.join("assets","wn.png"))

    def __init__(self, colour):
        pass