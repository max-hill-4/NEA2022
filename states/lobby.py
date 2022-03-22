import pygame as py
import tools as tl
import config as cfg
import database as db
import network as nt


class Lobby:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.text_box = tl.InputBox(150, 300)
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.button_confirm = tl.Button(cfg.button_confirm_image, 400, 300)
        self.button_create = tl.Button(cfg.button_create_image, 270, 150)
        self.object_list = (self.text_box, self.button_back,
                            self.button_confirm, self.button_create)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "LOGIN"

        if self.button_create.pressed(event):
            self.next_state = "WAIT"

        if self.button_confirm.pressed(event):
            if db.check_data('Gamelobby', self.text_box.text):
                ip = db.get_data('Gamelobby', 'IP',
                                 'GamelobbyID', self.text_box.text)
                nt.client_connect(ip[0][0])
                self.next_state = "GAMEPLAY"

        self.text_box.run(event)

    def draw(self, window):

        window.blit(cfg.background_lobby, (0, 0))

        for n in self.object_list:
            n.draw(window)
