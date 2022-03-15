import pygame as py
import tools as tl
import config as cfg


class Gameplay(object):
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        print(cfg.socket_object)
        if self.button_back.pressed(event):
            self.next_state = "MENU"

    def draw(self, window):

        window.blit(cfg.background_gameplay, (0, 0))
        self.button_back.draw(window)
