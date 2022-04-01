import pygame as py
import config as cfg


class InputBox:
    """Creates box with positional parameters
    to display what the user is typing on
    in window.
    """

    def __init__(self, xpos, ypos, hidden=False):

        self.xpos = xpos
        self.ypos = ypos
        self.image = cfg.text_box
        self.selected = False
        self.text = ''
        self.hidden = hidden

    def run(self, event):
        """
        """
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if (self.xpos < pos[0] < self.xpos + cfg.text_box_width and
                    self.ypos < pos[1] < self.ypos + cfg.text_box_height):
                self.selected = True
                self.image = cfg.text_box_selected

            else:
                self.selected = False
                self.image = cfg.text_box

        if self.selected:
            if event.type == py.KEYDOWN:

                if event.key == py.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, surface):
        surface.blit(self.image, (self.xpos, self.ypos))
        text_surface = cfg.font.render(self.text, True, (0, 0, 0))
        if self.hidden:
            text_surface = cfg.font.render(len(self.text)*'*', True, (0, 0, 0))

        surface.blit(text_surface, (self.xpos + 10, self.ypos + 10))


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

    def pressed(self, event):
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


class Gameboard:
    def __init__(self):
        self.object_list = {}
        self.object_list_values = list(self.object_list.values())
        self.draw_list = []
        for x in cfg.gameboard_row:
            for y in cfg.gameboard_column:
                self.object_list[x+y] = Button(cfg.blank,
                                               cfg.gameboard_row[x],
                                               cfg.gameboard_column[y])
        self.object_list_values = list(self.object_list.values())

    def update(self):

        for index, value in enumerate(cfg.game_data[2]):
            if value == 1:
                self.draw_list.append(self.object_list_values[index])
                self.draw_list[-1].image = cfg.cross
            if value == 2:
                self.draw_list.append(self.object_list_values[index])
                self.draw_list[-1].image = cfg.nought


def is_win(game_data):
    for win in cfg.nought_wins + cfg.cross_wins:
        count = 0
        for index, data in enumerate(win):
            if data == game_data[index] and data != 0:
                count += 1
            if count == 3:
                if data == cfg.player:
                    cfg.winner = True
                return data
