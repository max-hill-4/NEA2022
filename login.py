import sys
sys.path.append('E:\\modules')
import pygame as py
import tools as tl
import config as cfg
from database import Database as db

class Login(object):
    def __init__(self):
        self.done = False
        self.next_state = None

        self.text_box_username = tl.InputBox(50, 200)
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.button_confirm = tl.Button(cfg.button_confirm_image, 400, 200)
        self.object_list = (self.text_box_username, self.button_back,
                            self.button_confirm)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_back.pressed(event):
            self.next_state = "MENU"

        if self.button_confirm.pressed(event):

            if not db().check_data(self.text_box_username.text):
                db().add_data(self.text_box_username.text, 0)
   
            username = self.text_box_username.text
            self.next_state = "LOBBY"

        self.text_box_username.run(event)

    def draw(self, window):

        window.blit(cfg.background_login, (0, 0))

        for n in self.object_list:
            n.draw(window)
