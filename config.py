import pygame as py
py.init()

# Window size

width, height = 640, 480
window = py.display.set_mode((width, height))

# Init gameboard varaibles
gameboard_position = 175, 20
gameboard_row = {'row_0': 180, 'row_1': 280, 'row_2': 380}
gameboard_column = {'col_0': 25, 'col_1': 125, 'col_2': 225}
lobby_id = None
game_data = None, None, None
player = 1
winner = False

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
button_login_image = py.image.load("data/button_login.png").convert_alpha()
button_create_image = py.image.load("data/button_create.png").convert_alpha()
button_quit_image = py.image.load("data/button_quit.png").convert_alpha()
button_back_image = py.image.load("data/button_back.png").convert_alpha()
button_confirm_image = py.image.load("data/button_confirm.png").convert_alpha()

# Text box images
text_box = py.image.load("data/text_box.png").convert_alpha()
text_box_selected = py.image.load("data/text_box_outline.png").convert_alpha()

# Background images
background_title = py.image.load("data/background_title.png").convert_alpha()
background_login = py.image.load("data/background_login.png").convert_alpha()
background_lobby = py.image.load("data/background_lobby.png").convert_alpha()
background_wait = py.image.load("data/background_wait.png").convert_alpha()
background_gameplay = py.image.load("data/background_game.png").convert_alpha()
background_win = py.image.load("data/background_win.png").convert_alpha()
background_lose = py.image.load("data/background_lose.png").convert_alpha()

# Player images
cross = py.image.load("data/cross.png").convert_alpha()
nought = py.image.load("data/nought.png").convert_alpha()
gameboard = py.image.load("data/gameboard.png").convert_alpha()
blank = py.image.load("data/blank.png").convert_alpha()

# Caption string to get called
caption = "Noughts and Crosses"
# sizes of buttons
text_box_width, text_box_height = text_box.get_width(), text_box.get_height()

# Init pygame font
font = py.font.Font(None, 32)
