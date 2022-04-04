import pygame as py
import tools as tl
import config as cfg
import network as nt

class Wait:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back, 0, 0)
        self.font = py.font.Font("data/font.ttf", 28)
    
    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        if cfg.game_data[1]:
            self.next_state = "GAMEPLAY"

        if self.button_back.pressed(event):
            cfg.get_data = False
            nt.close()
            self.next_state = "LOBBY"

    def state_draw(self, window):


        text_surface = self.font.render('CODE: ' + cfg.lobby_id, True, (183, 60, 60))


        window.blit(cfg.background_wait, (0, 0))
        window.blit(text_surface, (190, 270))
        self.button_back.draw(window)
