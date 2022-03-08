import pygame as py 
from tools import *
import sys

class Login(object):
    def __init__(self):
        
        self.done = False
        self.next_state = None

        
        self.text_box_username = InputBox(200, 200)
        self.text_box_password = InputBox(200, 300, True)
        self.button_back = Button(button_back_image, 0, 0)
        self.button_confirm = Button(button_confirm_image, 270, 400)
        self.object_list = (self.text_box_username, self.text_box_password, self.button_back, self.button_confirm) 
    
    def get_event(self, event):
        
        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_back.pressed():
            self.next_state = "MENU"

        if self.button_confirm.pressed():
            print("confirm press")

        self.text_box_password.run(event)
        self.text_box_username.run(event)

    def draw(self, window):

        window.fill(login_screen_color)

        for n in self.object_list:
            n.draw(window)

        