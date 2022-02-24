import pygame as py
# Private Libraries
from utils import *
from database import Database


class Game:
	def __init__(self,surface):
		self.window = surface

	def lobby_screen(self):

		text_box_lobby = InputBox(200, 200)
		button_confirm = Button(button_confirm_image, 270, 400)

		object_list =(text_box_lobby, button_confirm)
		while True:
			
			for n in object_list:
			    n.draw(self.window)
			
			self.window.fill(TITLE__SCREEN_COLOR)
			
			py.display.update()

			for event in py.event.get():
			    if event.type == py.QUIT:
			        self.quit_screen()