import pygame as py
import tools as tl
import config as cfg


class Menu:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_login = tl.Button(cfg.button_login_image, 110, 300)
        self.button_quit = tl.Button(cfg.button_quit_image, 430, 300)
        self.object_list = (self.button_login, self.button_quit)

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        if self.button_login.pressed(event):
            self.next_state = "LOGIN"

        if self.button_quit.pressed(event):
            self.done = True

    def draw(self, window):

        window.blit(cfg.background_title, (0, 0))
        for n in self.object_list:
            n.draw(window)
