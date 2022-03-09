import sys
import pygame as py
import tools as tl
import config as cfg


class Create(object):
    def __init__(self):

        self.done = False
        self.next_state = None
        self.text_box_username = tl.InputBox(200, 200)
        self.text_box_password = tl.InputBox(200, 300)
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.button_confirm = tl.Button(cfg.button_confirm_image, 300, 400)

        self.object_list = (self.text_box_username, self.text_box_password,
                            self.button_back, self.button_confirm)

    def get_event(self, event):

        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_back.pressed(event):
            self.next_state = "LOGIN"

        if self.button_confirm.pressed(event):
            print("confirm press")

        self.text_box_username.run(event)
        self.text_box_password.run(event)

    def draw(self, window):

        window.blit(cfg.background_create, (0, 0))

        for n in self.object_list:
            n.draw(window)
