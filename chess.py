from engine import Chess_Engine
import pygame as pg
from board import Board
from engine import Chess_Engine

pg.init()

class Chess:
    def __init__(self, settings):
        self.settings = settings
        self.window = pg.display.set_mode(settings["window_size"])
        self.clock = pg.time.Clock()
        pg.display.set_caption("Chess v0.4")
        self.board = Board(settings)
        self.engine = Chess_Engine()

    
    def run(self):
        running = True
        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.board.set_FEN(self.engine.get_current_FEN())


            self.window.fill(self.settings["bg_colour"])
            self.window.blit(self.board.surface, self.settings["board_position"])
            
            pg.display.flip()
            self.clock.tick(60)
            