import os
import pygame as pg


class Pawn:
    
    IMG_B = pg.image.load(os.path.join("assets","bp.png"))
    IMG_W = pg.image.load(os.path.join("assets","wp.png"))

    def __init__(self, colour):
        pass