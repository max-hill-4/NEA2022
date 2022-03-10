import sys
sys.path.append('E:\\modules')

import pygame as py
import tools as tl
import config as cfg


class Menu(object):
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_login = tl.Button(cfg.button_login_image, 260, 250)
        self.button_quit = tl.Button(cfg.button_quit_image, 260, 300)
        self.object_list = (self.button_login, self.button_quit)

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_login.pressed(event):
            self.next_state = "LOGIN"

        if self.button_quit.pressed(event):
            self.done = True
            sys.exit()

    def draw(self, window):

        window.blit(cfg.background_title, (0, 0))

        for n in self.object_list:
            n.draw(window)
