    
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Maxwell Hill"
__license__ = "GPL"
__email__ = "maxwellhill2004@icloud.com"

# Public Libraries
import sys 
sys.path.append('E:\modules')
import pygame as py
 


# Private Libraries
from utils import *
from database import Database
from game import Game

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
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit_screen()

                if button_login.pressed(event):
                    self.login_screen()

                if button_create.pressed(event):
                    self.create_screen()

                if button_quit.pressed(event):
                    self.quit_screen()


    def login_screen(self):
      
        text_box_username = InputBox(200, 200)
        text_box_password = InputBox(200, 300, True)
        button_back = Button(button_back_image, 0, 0)
        button_confirm = Button(button_confirm_image, 270, 400)
        object_list = (text_box_username, text_box_password, button_back, button_confirm) 

        while True:

            self.window.fill(LOGIN_SCREEN_COLOR)    
            self.window.blit(title_login_image, (220, 75))
            for n in object_list:
                n.draw(self.window)
            
            py.display.update()

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit_screen()
                
                text_box_username.handle(event)
                text_box_password.handle(event)

                if button_back.pressed(event):
                    self.title_screen()

                if button_confirm.pressed(event):
                    if Database().check_data(text_box_username.text):
                    	if Database().check_data(text_box_password.text):
                            print('both fields have been found')
                            Game(self.window).lobby_screen()
                    		

    def create_screen(self):
        text_box_username = InputBox(200, 200)
        text_box_password = InputBox(200, 300, True)
        button_back = Button(button_back_image, 0, 0)
        button_confirm = Button(button_confirm_image, 270, 400)
        object_list = (text_box_username, text_box_password, button_back, button_confirm) 

        while True:

            self.window.fill(CREATE_SCREEN_COLOR)    
            self.window.blit(title_create_image, (220, 75))
            for n in object_list:
                n.draw(self.window)
            
            py.display.update()

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit_screen()
                
                text_box_username.handle(event)
                text_box_password.handle(event)

                if button_back.pressed(event):
                    self.title_screen()

                if button_confirm.pressed(event):
                    Database().add_data(text_box_username.text, text_box_password.text)

           

    def quit_screen(self):
        print("quit_screen")
        quit()


if __name__ == '__main__':   
    Menu().title_screen()

   
