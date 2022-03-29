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

        game_data = nt.get_data(cfg.lobby_id)
        print('finished getting data!')

        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "MENU"

        if game_data[0] == cfg.player:
            for index, data in enumerate(self.gameboard.object_list):
                if self.gameboard.object_list[data].pressed(event):
                    game_data[2][index] = cfg.player
                    nt.update_lobby(cfg.lobby_id, 2, game_data[2])
                    move = 2 if cfg.player == 1 else 1
                    nt.update_lobby(cfg.lobby_id, 0, move)

        self.gameboard.update(game_data[2])
        print(' end of get event loop !')
        if tl.is_win(game_data[2], cfg.cross_wins):
            print('cross wins!')

        if tl.is_win(game_data[2], cfg.nought_wins):
            print('nought wins!')

    def state_draw(self, window):

        window.blit(cfg.background_gameplay, (0, 0))

        for n in self.gameboard.draw_list:
            n.draw(window)

        window.blit(cfg.gameboard, (cfg.gameboard_position))
        self.button_back.draw(window)
        print(' i have drawn all stuff to the screen :)')
