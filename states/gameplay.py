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

        # If its your move
        if cfg.game_data[0] == cfg.player:
            for index, data in enumerate(self.gameboard.object_list):
                if self.gameboard.object_list[data].pressed(event):
                # If any of the squares are pressed
                    # change the game data
                    cfg.game_data[2][index] = cfg.player
                    # send the new game data to the server
                    nt.update_lobby(cfg.lobby_id, 2, cfg.game_data[2])
                    # changes the player move to enemy
                    move = 2 if cfg.player == 1 else 1
                    nt.update_lobby(cfg.lobby_id, 0, move)

        self.gameboard.update(cfg.game_data[2])
        
        if tl.is_win(cfg.game_data[2]):
            cfg.winner = True
            self.next_state = "RESULT"

    def state_draw(self, window):

        window.blit(cfg.background_gameplay, (0, 0))

        for n in self.gameboard.draw_list:
            n.draw(window)

        window.blit(cfg.gameboard, (cfg.gameboard_position))
        self.button_back.draw(window)
