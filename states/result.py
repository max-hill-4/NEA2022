import pygame as py
import tools as tl
import config as cfg
import network as nt

class Result:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_play = tl.Button(cfg.images['button_replay'], 270, 200)
        self.button_highscores = tl.Button(cfg.images['button_highscores'], 270, 250)
        self.button_quit = tl.Button(cfg.images['button_quit'], 270, 300)
        self.object_list = (self.button_play, self.button_quit,
                            self.button_highscores)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_play.pressed(event):
            
            try:
                if cfg.player == 1:
                    cfg.game_data[1] = False
                    nt.update_lobby(1, False)
                    nt.update_lobby(2, [0, 0, 0, 0, 0, 0, 0, 0, 0])
                    self.next_state = "WAIT"
                if cfg.player == 2:
                    if cfg.game_data[1] == False:
                        nt.update_lobby(1, True)
                        self.next_state = "WAIT"
            except:
                cfg.game_data = 1, False, [0, 0, 0, 0, 0, 0, 0, 0, 0] 
                self.next_state = "LOCAL"

        if self.button_highscores.pressed(event):
            self.next_state = "HIGHSCORES"
    
    def state_draw(self, window):
        image = cfg.images['win'] if cfg.winner is True else cfg.images['lose']
        window.blit(cfg.images['background_blank'], (0, 0))
        window.blit(image, (130, 50))
        for n in self.object_list:
            n.draw(window)
