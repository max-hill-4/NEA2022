import pygame as py
import tools as tl
import config as cfg
import network as nt


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

        for index, data in enumerate(self.gameboard.object_list):
            # if cfg.move:
            if self.gameboard.object_list[data].pressed(event):
                data = nt.get_data(cfg.lobby_id)[1]
                data[index] = 1
                nt.update_lobby(cfg.lobby_id, 1, data)
                cfg.move = False

    def draw(self, window):

        window.blit(cfg.background_gameplay, (0, 0))

        for n in self.gameboard.draw_list:
            n.draw(window)

        window.blit(cfg.gameboard, (cfg.gameboard_position))
        self.gameboard.update(nt.get_data(cfg.lobby_id)[1])
        self.button_back.draw(window)
