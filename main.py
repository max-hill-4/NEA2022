
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Maxwell Hill"
__license__ = "GPL"
__email__ = "maxwellhill2004@icloud.com"

#push test

# Public Libraries
import pygame as py

# Private Libraries
from utils import *


class Game:

    def __init__(self):

        py.display.set_caption(caption)
        self.window = py.display.set_mode((width, height), vsync=1)

    def title_screen(self):

        self.state = -1

        loginButton = Button(button_login_image, width*0.25 -
                             (titleButtonWidth/2), height * 0.625)
        createButton = Button(button_create_image, width *
                              0.5 - (titleButtonWidth/2), height * 0.625)
        quitButton = Button(button_quit_image, width*0.75 -
                            (titleButtonWidth/2), 300)
        # Loops whilst the title_screen is being shown.
        while self.state == -1:

            # Displays logo on the screen
            self.window.fill(titleScreenColor)
            self.window.blit(
                title_name_image, (midWidth - titleNameWidth/2, 100))

            loginButton.draw(self.window)
            createButton.draw(self.window)
            quitButton.draw(self.window)

            # Updating the window once buttons are written to the window.
            py.display.update()

            for event in py.event.get():
                # print(event)
                if event.type == py.QUIT:
                    self.quit_screen()

                if Button.pressed(loginButton):
                    self.login_screen()

                if Button.pressed(createButton):
                    self.create_screen()

                if Button.pressed(quitButton):
                    self.quit_screen()

    def login_screen(self):
        """ Function that handles logging into 
        your account and checks user input
        against a database.
        """

        self.state = 0
        usernametextBox = InputBox(200, 200)
        passwordtextBox = InputBox(200, 300, True)
        backButton = Button(button_back_image, 0, 0)
        confirmButton = Button(button_confirm_image, 250, 400)
        while self.state == 0:

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit_screen()

                if Button.pressed(backButton):
                    self.state = -1
                    self.title_screen()

                if Button.pressed(confirmButton):
                    pass
                usernametextBox.handle(event)
                passwordtextBox.handle(event)

            self.window.fill(titleScreenColor)
            backButton.draw(self.window)
            usernametextBox.draw(self.window)
            passwordtextBox.draw(self.window)
            confirmButton.draw(self.window)
            py.display.update()

    def create_screen(self):
        print("create_screen")

    def quit_screen(self):
        print("quit_screen")
        quit()


""" Instance of a game created named g, although
pygame is unable to create multiple windows in the same instance,
using a class much easier for menu cycling.
"""
h = Game()
h.title_screen()
