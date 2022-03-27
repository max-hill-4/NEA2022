import pygame as py
import tools as tl
import config as cfg
import network as nt


class Wait:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.lobby_created = False
        self.lobby_id = None

    def get_event(self, event):
        if event.type == py.QUIT:
            # nt.del_lobby(self.lobby_id)
            self.lobby_created = False
            self.done = True

        if not self.lobby_created:
            print('creating game lobby')
            self.lobby_id = nt.lobby_code()
            nt.add_lobby(self.lobby_id)
            self.lobby_created = True

        print(nt.get_data(self.lobby_id)[0])
        # if nt.get_data(self.lobby_id)[0]:
        #     print('user connected!')

        if self.button_back.pressed(event):
            # nt.del_data(self.lobby_id)
            self.lobby_created = False
            self.next_state = "LOBBY"

    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))
        self.button_back.draw(window)
