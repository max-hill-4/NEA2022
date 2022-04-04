import pygame as py
import tools as tl
import config as cfg
import network as nt
import threading as th


class Lobby:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.text_box = tl.InputBox(150, 300)
        self.button_back = tl.Button(cfg.button_back, 0, 0)
        self.button_confirm = tl.Button(cfg.button_confirm, 400, 300)
        self.button_create = tl.Button(cfg.button_create, 270, 150)
        self.object_list = (self.text_box, self.button_back,
                            self.button_confirm, self.button_create)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "LOGIN"

        if self.button_create.pressed(event):
            # cfg.lobby_id = nt.lobby_code()
            try:
                nt.connect_server()
                nt.create_lobby()
                cfg.get_data = True
                t = th.Thread(target=nt.get_data)
                t.start()
                self.next_state = "WAIT"
            except Exception as e:
                print(e, 'server is not online.')

        if self.button_confirm.pressed(event):
            nt.connect_server()
            if nt.check_data(self.text_box.text):
                cfg.lobby_id = self.text_box.text
                nt.update_lobby(1, True)

                t = th.Thread(target=nt.get_data)
                t.start()

                cfg.player = 2
                self.next_state = "GAMEPLAY"

            else:
                print('no lobby found')

        self.text_box.run(event)

    def state_draw(self, window):

        window.blit(cfg.background_lobby, (0, 0))

        for n in self.object_list:
            n.draw(window)
