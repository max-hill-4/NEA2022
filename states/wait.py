import pygame as py
import tools as tl
import config as cfg
import network as nt


class Wait:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.game_lobby = nt.create_gamelobby()

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "LOBBY"

    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))
        self.button_back.draw(window)
