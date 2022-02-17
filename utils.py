import pygame as py
from config import *


class InputBox:
    """Creates box with positional parameters
    to display what the user is typing on 
    in window.
    """

    def __init__(self, xpos, ypos, hidden=False):

        self.xpos = xpos
        self.ypos = ypos
        self.buttonWidth = text_box_image.get_width()
        self.buttonHeight = text_box_image.get_height()
        self.image = text_box_image
        self.selected = False
        self.text = ''
        self.hidden = hidden

    def handle(self, event):
        """ 
        """
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if (self.xpos < pos[0] < self.xpos + self.buttonWidth) and (self.ypos < pos[1] < self.ypos + self.buttonHeight):
                self.selected = True
                self.image = text_box_image_selected

            else:
                self.selected = False
                self.image = text_box_image

        if self.selected:
            if event.type == py.KEYDOWN:

                if event.key == py.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, surface):
        surface.blit(self.image, (self.xpos, self.ypos))
        textSurface = font.render(self.text, True, (0, 0, 0))
        if self.hidden == True:
            textSurface = font.render(len(self.text)*'*', True, (0, 0, 0))

        surface.blit(textSurface, (self.xpos + 10, self.ypos + 10))


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

    def pressed(self,event):
        """ Uses inbuilt
         pygame method to check if 
        the left mouse button is being pressed down
        if it is being pressed it checks if the mouse is 
        hovering over the button if it is then it returns True
        """
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if self.xpos < pos[0] < self.xpos + self.buttonWidth:
                if self.ypos < pos[1] < self.ypos + self.buttonHeight:
                    return True

    def draw(self, surface):
        surface.blit(self.image, (self.xpos, self.ypos))
