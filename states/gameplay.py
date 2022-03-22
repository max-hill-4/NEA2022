import pygame as py
import tools as tl
import config as cfg


class Gameplay:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.gameboard = tl.Gameboard()

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "MENU"

    def draw(self, window):

        window.blit(cfg.background_gameplay, (0, 0))
        self.gameboard.draw(window)
        self.button_back.draw(window)
