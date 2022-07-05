import os
import pygame as pg


class King:
    
    IMG_B = pg.image.load(os.path.join("assets","bk.png"))
    IMG_W = pg.image.load(os.path.join("assets","wk.png"))

    def __init__(self, colour):
        pass