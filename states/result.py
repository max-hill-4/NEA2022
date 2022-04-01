import pygame as py
import tools as tl
import config as cfg


class Result:
    def __init__(self):
        self.done = False
        self.next_state = None

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

    def state_draw(self, window):
        
        if cfg.winner:
            window.blit(cfg.background_win, (0, 0))

        else:
            window.blit(cfg.background_lose, (0, 0))
