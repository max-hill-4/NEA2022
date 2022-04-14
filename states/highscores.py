import pygame as py
import tools as tl
import config as cfg
import database as db

class Highscores:
    def __init__(self):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back, 0, 0)
        self.font = py.font.Font("data/font.ttf", 12)
    def get_event(self, event):
        if event.type == py.QUIT:
            self.done = True

        
        if self.button_back.pressed(event):
            self.next_state = "RESULT"

    def state_draw(self, window):

        data = db.fetch_data()
        table_x = 200
        table_y = 30
        window.blit(cfg.background_blank, (0, 0))
        self.button_back.draw(window)
        for record in data:
            username = self.font.render(record[0], True, (183, 60, 60))
            score = self.font.render(str(record[1]), True, (183, 60, 60))
            
            window.blit(username, (table_x, table_y))
            window.blit(score, (table_x + 200, table_y))
            table_y += 30