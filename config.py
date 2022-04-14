import pygame as py
import os
py.init()

# Window size

width, height = 640, 480
window = py.display.set_mode((width, height))
py.display.set_caption("Noughts and Crosses")
# Init gameboard varaibles
gameboard_position = 175, 20
gameboard_row = {'row_0': 180, 'row_1': 280, 'row_2': 380}
gameboard_column = {'col_0': 25, 'col_1': 125, 'col_2': 225}

# 
# these variables trigger me a bit - global for diffrent parts int he game.
lobby_id = None
game_data = 1, False, [0, 0, 0, 0, 0, 0, 0, 0, 0]
player = 1
winner = False
get_data = True
username = None

cross_wins = [
    (1, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 1),

    (1, 0, 0, 1, 0, 0, 1, 0, 0),
    (0, 1, 0, 0, 1, 0, 0, 1, 0),
    (0, 0, 1, 0, 0, 1, 0, 0, 1),

    (1, 0, 0, 0, 1, 0, 0, 0, 1),
    (0, 0, 1, 0, 1, 0, 1, 0, 0),
]

nought_wins = [tuple(2 if y else 0 for y in x) for x in cross_wins]

# Button images
files =[
"button_login.png",
"button_create.png",
"button_quit.png",
"button_back.png",
"button_confirm.png",
"button_highscores.png",
"button_replay.png",
"button_local.png",
"text_box.png",
"text_box_outline.png",
"background_title.png",
"background_login.png",
"background_lobby.png",
"background_wait.png",
"background_game.png",
"background_blank.png",
"cross.png",
"nought.png",
"gameboard.png",
"blank.png",
"win.png",
"lose.png",
]
images = {}

for filepath in files:
    path = filename = os.path.basename(filepath)
    name, ext = os.path.splitext(path)
    image = py.image.load(os.path.join('data', filepath)).convert_alpha()
    images[name] = image