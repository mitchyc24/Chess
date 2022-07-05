import os
import pygame as pg


class Queen:
    
    IMG_B = pg.image.load(os.path.join("assets","bq.png"))
    IMG_W = pg.image.load(os.path.join("assets","wq.png"))

    def __init__(self, colour):
        pass