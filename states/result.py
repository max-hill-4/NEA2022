import pygame as py
import tools as tl
import config as cfg
import network as nt

class Result:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_play = tl.Button(cfg.button_replay, 110, 300)
        self.button_highscores = tl.Button(cfg.button_highscores, 430, 300)
        self.button_quit = tl.Button(cfg.button_quit, 500, 200)
        self.object_list = (self.button_play, self.button_quit,
                            self.button_highscores)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_play.pressed(event):
            
            if cfg.player == 1:
                cfg.game_data[1] = False
                nt.update_lobby(1, False)
                nt.update_lobby(2, [0, 0, 0, 0, 0, 0, 0, 0, 0])
                self.next_state = "WAIT"
            else:
                if cfg.game_data[1] == False:
                    nt.update_lobby(1, True)
                    self.next_state = "WAIT"
                    
        if button_highscores.pressed(event):
            self.next_state = "LOBBY"

        if button_highscores.pressed(event):
            self.next_state = "HIGHSCORES"
    
    def state_draw(self, window):
        image = cfg.image_win if cfg.winner is True else cfg.image_lose
        window.blit(cfg.background_blank, (0, 0))
        window.blit(image, (130, 50))
        for n in self.object_list:
            n.draw(window)
