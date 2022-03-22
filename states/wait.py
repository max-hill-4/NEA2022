import pygame as py
import tools as tl
import config as cfg
import threading as th
import database as db
import network as nt


class Wait:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.server_running = False
        self.game_lobby = None

    def get_event(self, event):
        if event.type == py.QUIT:
            db.del_data('Gamelobby', 'GamelobbyID', self.game_lobby)
            nt.close()
            self.done = True

        if not self.game_lobby:
            self.game_lobby = db.create_gamelobby()
            print(self.game_lobby)

        if not self.server_running:
            nt.build_server()
            t = th.Thread(target=nt.connection_attempt)
            t.start()
            self.server_running = True

        if self.button_back.pressed(event):

            db.del_data('Gamelobby', 'GamelobbyID', self.game_lobby)
            self.game_lobby = None
            nt.close()
            self.server_running = False
            self.next_state = "LOBBY"

        if cfg.connection:
            cfg.user_image = cfg.cross
            self.next_state = "GAMEPLAY"

    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))
        self.button_back.draw(window)