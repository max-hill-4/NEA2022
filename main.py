
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Maxwell Hill"
__license__ = "GPL"
__email__ = "maxwellhill2004@icloud.com"

# Public Libraries
import pygame as py

# Private Libraries
from utils import *

class Menu:

    def __init__(self):

        self.window = py.display.set_mode((width, height))
        py.display.set_caption(CAPTION)
    
    def title_screen(self):

        button_login = Button(button_login_image, 110, 300)
        button_create = Button(button_create_image, 270, 300)
        button_quit = Button(button_quit_image, 430, 300)
        object_list = (button_login, button_create, button_quit)

        while True:

            self.window.fill(TITLE__SCREEN_COLOR)
            self.window.blit(title_name_image, (220, 100))

            for n in object_list:
                n.draw(self.window)

            py.display.update()

            if button_login.pressed():
                self.login_screen()

            if button_create.pressed():
                self.create_screen()

            if button_quit.pressed():
                self.quit_screen()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit_screen()


    def login_screen(self):
        """ Function that handles logging into 
        your account and checks user input
        against a database.
        """
        text_box_username = InputBox(200, 200)
        text_box_password = InputBox(200, 300, True)
        button_back = Button(button_back_image, 0, 0)
        button_confirm = Button(button_confirm_image, 250, 400)
        object_list = (text_box_username, text_box_password, button_back, button_confirm) 

        while True:

            self.window.fill(LOGIN_SCREEN_COLOR)    
           
            for n in object_list:
                n.draw(self.window)
            
            py.display.update()
            
            if Button.pressed(button_back):
                self.title_screen()

            if Button.pressed(button_confirm):
                pass

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit_screen()
                
                text_box_username.handle(event)
                text_box_password.handle(event)

            
            

    def create_screen(self):
        print("create_screen")

    def quit_screen(self):
        print("quit_screen")
        quit()


""" Instance of a game created named g, although
pygame is unable to create multiple windows in the same instance,
using a class much easier for menu cycling.
"""

if __name__=='__main__':
    h = Menu()
    h.title_screen()
