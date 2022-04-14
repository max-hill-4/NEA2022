import pygame as py
import tools as tl
import config as cfg


class Local:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.images['button_back'], 0, 0)
        self.gameboard = tl.Gameboard()
    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "LOBBY"

        for index, data in enumerate(self.gameboard.object_list):
                if self.gameboard.object_list[data].pressed(event):
                    cfg.game_data[2][index] = cfg.player
                    cfg.player = 2 if cfg.player == 1 else 1

        if tl.is_win():
            self.next_state = "RESULT"
    def state_draw(self, window):
        
        window.blit(cfg.images['background_blank'], (0, 0))

        self.gameboard.draw(window)  
        self.button_back.draw(window)
