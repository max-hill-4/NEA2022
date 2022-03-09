
import pygame as py 
from tools import *
import sys


class Menu(object):
    def __init__(self):
        py.init()  
        self.done = False
        self.next_state = None
        self.button_login = Button(button_login_image, 110, 300)
        self.button_quit = Button(button_quit_image, 430, 300)
        self.object_list = (self.button_login, self.button_quit)
        
    
    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_login.pressed(event):
            print("press")
            self.next_state = "LOGIN"


        if self.button_quit.pressed(event):
            self.done = True
            sys.exit()
    def draw(self, window):

        window.fill(title_screen_color)
        window.blit(title_name_image, (220, 100))

        for n in self.object_list:
            n.draw(window)
