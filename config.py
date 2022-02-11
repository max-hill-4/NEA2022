#config
import pygame as py
py.init()
# Window size.
width ,height = 640,480
midWidth , midHeight = width/2 , height/2
titleScreenColor=(100,200,255)
loginScreenColor=(255,80,150)
# Pygame creates  hidden surface ready to be shown on screen.
titleScreenLogin = py.image.load("recources/titleScreenLogin.png")
titleScreenCreate = py.image.load("recources/titleScreenCreate.png")
titleScreenQuit = py.image.load("recources/titleScreenQuit.png")
titleScreenName = py.image.load("recources/titleScreenName.png")
backButtonImage = py.image.load("recources/backButton.png")
textBoxImageUnselected = textBoxImage = py.image.load("recources/textBox.png")
textBoxImageSelected = py.image.load("recources/textBoxSelected.png")
fullscreenImage = py.image.load("recources/fullscreen.png")
# Button size.
titleButtonWidth = titleScreenLogin.get_width()
titleButtonHeight = titleScreenLogin.get_height()
titleNameWidth = titleScreenName.get_width() 
titleNameHeight = titleScreenName.get_height()
caption = "Noughts and Crosses"
font = py.font.Font(None, 32)


