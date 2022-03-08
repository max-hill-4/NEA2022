#config
import pygame as py
py.init()


# Window size.
width ,height = 640,480

title_screen_color=(100,200,255)
login_screen_color=(255,80,150)



# Pygame creates  hidden surface ready to be shown on screen.
button_login_image = py.image.load("resources/button_login_image.png")

button_create_image = py.image.load("resources/button_create_image.png")
button_quit_image = py.image.load("resources/button_quit_image.png")
button_back_image = py.image.load("resources/button_back_image.png")
button_confirm_image = py.image.load("resources/button_confirm_image.png")

text_box_image =  py.image.load("resources/text_box_image.png")
text_box_image_selected = py.image.load("resources/text_box_image_selected.png")

title_name_image = py.image.load("resources/title_name_image.png")






# Button size.
caption = "Noughts and Crosses"
font = py.font.Font(None, 32)


