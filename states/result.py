import pygame as py
import tools as tl
import config as cfg


class Result:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_play = tl.Button(cfg.button_login, 110, 300)
        self.button_highscores = tl.Button(cfg.button_quit, 430, 300)
        self.button_quit = tl.Button(cfg.button_quit, 430, 300)
        self.object_list = (self.button_play, self.button_quit, self.button_highscores)
        self.background =  cfg.background_win if cfg.winner else cfg.background_lose
    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

    def state_draw(self, window):
        
        window.blit(self.background, (0, 0))

        for n in self.object_list:
            n.draw(window)
    