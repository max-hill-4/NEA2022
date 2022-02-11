
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{Multiplayer Noughts and Crosses game for NEA 2022.}
{GPL}
"""
__author__ = "Maxwell Hill"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Maxwell Hill"
__email__ = "maxwellhill2004@icloud.com"
__status__ = "Production"


# Built-in/Generic Imports
import sys

# Libs
import pygame as py

# Own modules
from config import *


class InputBox:
    """Creates box with positional parameters
    to display what the user is typing on 
    in window.
    """

    def __init__(self, xpos, ypos):

        self.xpos = xpos
        self.ypos = ypos
        self.buttonWidth = textBoxImage.get_width()
        self.buttonHeight = textBoxImage.get_height()
        self.image = textBoxImageUnselected
        self.selected = False
        self.text = ''
    def handle(self,event):
        """ 
        """
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if self.xpos < pos[0] < self.xpos + self.buttonWidth and self.ypos < pos[1] < self.ypos + self.buttonHeight:
                self.selected = True
                self.image = textBoxImageSelected                    
            
            else:
                self.selected = False                 
                self.image = textBoxImageUnselected
        
        if event.type == py.KEYDOWN:

            if event.key == py.K_RETURN:
                    print(self.text)
                    self.text = '' 
            
            elif event.key == py.K_BACKSPACE:
                    self.text = self.text[:-1]
            else:
                self.text += event.unicode
            print(self.text)
    def draw(self):
        #print("sel")
        g.window.blit(self.image, (self.xpos, self.ypos))
        textSurface = font.render(self.text, True, (0,0,0))
        g.window.blit(textSurface, (self.xpos, self.ypos))

class Button:
    """ Takes image and positional paramaters and creates a pygame
    surface with a pressed method to check if the left moust button
    is pressed and the mouse position is ontop the surface.
    """

    def __init__(self, image, xpos, ypos):
        """ Constructor method that sets parameters as attributes
        and also displays the image ontop of the screen.
        """
        self.xpos = xpos
        self.ypos = ypos
        self.buttonWidth = image.get_width()
        self.buttonHeight = image.get_height()
        self.image = image
  
    def pressed(self):
        """ Uses inbuilt
         pygame method to check if 
        the left mouse button is being pressed down
        if it is being pressed it checks if the mouse is 
        hovering over the button if it is then it returns True
        """
        if py.mouse.get_pressed()[0] == True:
            pos = py.mouse.get_pos()
            if self.xpos < pos[0] < self.xpos + self.buttonWidth:
                if self.ypos < pos[1] < self.ypos + self.buttonHeight:
                    return True
          
    def draw(self):
        g.window.blit(self.image, (self.xpos, self.ypos))

class Game:
    """ Main loop that handles 3 menus in the game and allowes the method
    to be called to write over the surfaces and reset the window allowing
    for menu cycling.
    
    Window is called outside of the constructor because it is a class
    variable and shared between classes, needs to be a variable
    """
    window = py.display.set_mode((width, height),vsync=1)
    # py.SCALED,
    def __init__(self):
        """ Contructor initialses pygame and creates the window."""
        #py.init()
        py.display.set_caption(caption)
        self.state = -1
        self.fullscreen = False
    def titleScreen(self):
        """ Default screen to show when the game is started."""
        
        

        # titleScreen = -1
        # loginScreen = 0
        # createScreen = 1

        loginButton = Button(titleScreenLogin, width*0.25 - (titleButtonWidth/2), height * 0.625)
        createButton = Button(titleScreenCreate, width*0.5 - (titleButtonWidth/2) , height * 0.625)
        quitButton = Button(titleScreenQuit, width*0.75 - (titleButtonWidth/2), 300)
        fullscreenButton = Button(fullscreenImage,width - 30, 0 )
        # Loops whilst the titleScreen is being shown.
        while self.state == -1:

            # Displays logo on the screen
            self.window.fill(titleScreenColor)
            self.window.blit(titleScreenName, (midWidth - titleNameWidth/2 , 100))

            loginButton.draw()
            createButton.draw()
            quitButton.draw()
            fullscreenButton 

            # Updating the window once buttons are written to the window.
            py.display.update()

            for event in py.event.get():
                #print(event)
                if event.type == py.QUIT:
                    self.quitScreen()

                if Button.pressed(loginButton):
                    self.loginScreen()

                if Button.pressed(createButton):
                    self.createScreen()

                if Button.pressed(quitButton):
                    self.quitScreen()


                # if Button.pressed(fullscreenButton):
                #     if self.fullscreen == False:
                #         py.display.set_mode((width, height), FULLSCREEN)
                #         self.fullscreen = True

                #     elif self.fullscreen == True:
                #         py.display.set_mode((width, height))
                #         self.fullscreen = False
                #     if window.get_flags() & FULLSCREEN:
                #         py.display.set_mode((width, height))
                # else:
                #     py.display.set_mode((width, height), FULLSCREEN)

    def loginScreen(self):
        """ Function that handles logging into 
        your account and checks user input
        against a database.
        """
        
        self.state = 0
        usernametextBox = InputBox(200,200)
        passwordtextBox = InputBox(200,350)
        backButton = Button(backButtonImage, 0, 0)
        while self.state == 0:
    
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.quitScreen()

                if Button.pressed(backButton):
                    self.state= -1
                    self.titleScreen()
                usernametextBox.handle(event)
                passwordtextBox.handle(event)
            
            self.window.fill(titleScreenColor)  
            backButton.draw()
            usernametextBox.draw()
            passwordtextBox.draw()



            py.display.update()
       
    def createScreen(self):
        print("createScreen")

    def quitScreen(self):
        print("quitScreen")
        sys.exit()

""" Instance of a game created named g, although
pygame is unable to create multiple windows in the same instance,
using a class much easier for menu cycling.
"""
g = Game()
g.titleScreen()
