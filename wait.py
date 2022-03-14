import pygame as py
import tools as tl
import config as cfg


class Wait(object):
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_back.pressed(event):
            self.next_state = "LOBBY"


    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))

        self.button_back.draw(window)
