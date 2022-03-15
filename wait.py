import pygame as py
import tools as tl
import config as cfg
from network import Build_Server as nt
import threading as th


class Wait(object):
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.server_running = False

    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        if not self.server_running:
            self.server = nt()
            t = th.Thread(target=self.server.connection_attempt)
            t.start()
            self.server_running = True

        if self.button_back.pressed(event):
            self.server.close()
            self.server_running = False
            self.next_state = "LOBBY"

        if self.server.connection:
            cfg.socket_object = self.server.connection
            self.next_state = "GAMEPLAY"

    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))
        self.button_back.draw(window)
