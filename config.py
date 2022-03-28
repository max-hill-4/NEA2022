import pygame as py
py.init()

# Window size
width, height = 640, 480

# Init network variables

port, server = 5555, "141.147.118.101"

# Init gameboard varaibles
gameboard_position = 175, 20
gameboard_row = {'row_0': 180, 'row_1': 280, 'row_2': 380}
gameboard_column = {'col_0': 25, 'col_1': 125, 'col_2': 225}
lobby_id = None
move = None
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
button_login_image = py.image.load("resources/button_login.png").convert()
button_create_image = py.image.load("resources/button_create.png").convert()
button_quit_image = py.image.load("resources/button_quit.png").convert()
button_back_image = py.image.load("resources/button_back.png").convert()
button_confirm_image = py.image.load("resources/button_confirm.png").convert()

# Text box images
text_box = py.image.load("resources/text_box.png").convert()
text_box_selected = py.image.load("resources/text_box_outline.png").convert()

# Background images
background_title = py.image.load("resources/background_title.png").convert()
background_login = py.image.load("resources/background_login.png").convert()
background_lobby = py.image.load("resources/background_lobby.png").convert()
background_wait = py.image.load("resources/background_wait.png").convert()
background_gameplay = py.image.load("resources/background_game.png").convert()

# Player images
cross = py.image.load("resources/cross.png").convert()
nought = py.image.load("resources/nought.png").convert()
gameboard = py.image.load("resources/gameboard.png").convert()
# Caption string to get called
caption = "Noughts and Crosses"

# Init pygame font
font = py.font.Font(None, 32)
