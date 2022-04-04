import pygame as py
import tools as tl
import config as cfg


class Result:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_play = tl.Button(cfg.button_replay, 110, 300)
        self.button_highscores = tl.Button(cfg.button_highscores, 430, 300)
        self.button_quit = tl.Button(cfg.button_quit, 500, 200)
        self.object_list = (self.button_play, self.button_quit,
                            self.button_highscores)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_play.pressed(event):
            self.next_state = "GAMEPLAY"

    def state_draw(self, window):
        image = cfg.image_win if cfg.winner is True else cfg.image_lose
        window.blit(cfg.background_blank, (0, 0))
        window.blit(image, (50, 50))
        for n in self.object_list:
            n.draw(window)
