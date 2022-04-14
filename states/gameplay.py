import pygame as py
import tools as tl
import config as cfg
import network as nt


class Gameplay:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.images['button_back'], 0, 0)
        self.gameboard = tl.Gameboard()
        self.font = py.font.Font("data/font.ttf", 12)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "MENU"

        # If its your move
        if cfg.game_data[0] == cfg.player:
            for index, data in enumerate(self.gameboard.object_list):
                if self.gameboard.object_list[data].pressed(event):
                    # If any of the squares are pressed
                    # change the game data
                    move = 2 if cfg.player == 1 else 1
                    nt.update_lobby(0, move)
                    print(f'i have sent change move to {move}')
                    
                    cfg.game_data[2][index] = cfg.player
                    # send the new game data to the server
                    nt.update_lobby(2, cfg.game_data[2])
                    # changes the player move to enemy
                    
                    print("")
        if tl.is_win():
            self.next_state = "RESULT"

    def state_draw(self, window):

        window.blit(cfg.images['background_game'], (0, 0))

        self.gameboard.draw(window)        
        self.button_back.draw(window)
        
        # indicates whether its your move or opponents
        if cfg.game_data[0] == cfg.player:
            text = self.font.render('Your Move', True, (183, 60, 60))
        else:
            text = self.font.render('Not Your Move', True, (183, 60, 60))

        playertext = self.font.render(str(cfg.player), True, (183, 60, 60))
        window.blit(text, (20, 50))
        window.blit(playertext, (20, 80))
