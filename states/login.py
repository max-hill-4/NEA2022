import pygame as py
import tools as tl
import config as cfg
import database as db


class Login:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.text_box = tl.InputBox(50, 200)
        self.button_back = tl.Button(cfg.images['button_back'], 0, 0)
        self.button_confirm = tl.Button(cfg.images['button_confirm'], 400, 200)
        self.object_list = (self.text_box, self.button_back,
                            self.button_confirm)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True

        if self.button_back.pressed(event):
            self.next_state = "MENU"

        if self.button_confirm.pressed(event):

            if not db.check_data(self.text_box.text):
                print('new user created')
                db.add_username(self.text_box.text)

            cfg.username = self.text_box.text
            self.next_state = "LOBBY"

        self.text_box.run(event)

    def state_draw(self, window):

        window.blit(cfg.images['background_login'], (0, 0))

        for n in self.object_list:
            n.draw(window)
