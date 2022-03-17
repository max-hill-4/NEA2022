import sys
import pygame as py
import config
import menu
import login
import lobby
import wait
import gameplay

py.init()


window = py.display.set_mode((config.width, config.height))

states = {
    "MENU": menu.Menu(),
    "LOGIN": login.Login(),
    "LOBBY": lobby.Lobby(),
    "WAIT": wait.Wait(),
    "GAMEPLAY": gameplay.Gameplay()

}


class Game(object):
    def __init__(self, window, states, start_state):
        self.window = window
        self.states = states
        self.state = self.states[start_state]

    def event_loop(self):
        for event in py.event.get():
            self.state.get_event(event)

    def update(self):

        if self.state.next_state:
            change_state = self.state.next_state
            self.state.next_state = None
            self.state = self.states[change_state]

    def draw(self):
        self.state.draw(self.window)

    def run(self):
        while not self.state.done:
            self.event_loop()
            self.update()
            self.draw()
            py.display.update()
        py.quit()
        sys.exit()


game = Game(window, states, "MENU")
game.run()
