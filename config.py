#config
import pygame as py
py.init()
# Window size.

width ,height = 640,480

TITLE__SCREEN_COLOR = (100,200,255)
LOGIN_SCREEN_COLOR = (255,80,150)


# Images used for all buttons
button_login_image = py.image.load("resources/button_login_image.png")
button_create_image = py.image.load("resources/button_create_image.png")
button_quit_image = py.image.load("resources/button_quit_image.png")
button_back_image = py.image.load("resources/button_back_image.png")
button_confirm_image = py.image.load("resources/button_confirm_image.png")
# Images used for 2 states of InputBox
text_box_image =  py.image.load("resources/text_box_image.png")
text_box_image_selected = py.image.load("resources/text_box_image_selected.png")

title_name_image = py.image.load("resources/title_name_image.png")


# Button size.
titleButtonWidth = button_login_image.get_width()
titleButtonHeight = button_login_image.get_height()
titleNameWidth = title_name_image.get_width() 
titleNameHeight = title_name_image.get_height()

CAPTION = "Noughts and Crosses"
font = py.font.Font(None, 32)