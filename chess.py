from engine import Chess_Engine
import pygame as pg
from board import Board
from engine import Chess_Engine

pg.init()

class Chess:
    """
    Chess class is responsible for game flow and running mainloop. 
    """
    def __init__(self, settings):
        self.settings = settings
        self.window = pg.display.set_mode(settings["window_size"])
        self.clock = pg.time.Clock()
        pg.display.set_caption("Chess v0.1")
        self.board = Board(settings)
        self.engine = Chess_Engine()

    
    def run(self):
        running = True
        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = self._get_mouse_pos()

            self.board.set_FEN(self.engine.get_current_FEN())


            self.window.fill(self.settings["bg_colour"])
            self.window.blit(self.board.surface, self.settings["board_position"])
            
            pg.display.flip()
            self.clock.tick(60)
            

    def _get_mouse_pos(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_x -= self.settings["board_position"][0]
        mouse_y -= self.settings["board_position"][1]
        if 0 < mouse_x < self.settings["board_size"][0] and 0 < mouse_y < self.settings["board_size"][1]:
            return self.board.convert_board_pixels_to_pos((mouse_x,mouse_y))
        return None