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
# Button images
button_login_image = py.image.load("resources/button_login_image.png")
button_create_image = py.image.load("resources/button_create_image.png")
button_quit_image = py.image.load("resources/button_quit_image.png")
button_back_image = py.image.load("resources/button_back_image.png")
button_confirm_image = py.image.load("resources/button_confirm_image.png")

# Text box images
text_box_image = py.image.load("resources/text_box_image.png")
text_box_image_selected = py.image.load("resources/text_box_image_outline.png")

# Background images
background_title = py.image.load("resources/background_title.png")
background_login = py.image.load("resources/background_login.png")
background_lobby = py.image.load("resources/background_lobby.png")
background_wait = py.image.load("resources/background_wait.png")
background_gameplay = py.image.load("resources/background_gameplay.png")

# Player images
cross = py.image.load("resources/cross.png")
nought = py.image.load("resources/nought.png")
gameboard = py.image.load("resources/gameboard.png")
# Caption string to get called
caption = "Noughts and Crosses"

# Init pygame font
font = py.font.Font(None, 32)
