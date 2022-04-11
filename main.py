import pygame as py
import config as cfg
import states

py.init()

states = {
    "MENU": states.menu.Menu(),
    "LOGIN": states.login.Login(),
    "LOBBY": states.lobby.Lobby(),
    "WAIT": states.wait.Wait(),
    "GAMEPLAY": states.gameplay.Gameplay(),
    "RESULT": states.result.Result(),
    "LOCAL": states.local.Local()
}


class Game:
    def __init__(self, states, start_state):
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
        self.state.state_draw(cfg.window)

    def run(self):
        while not self.state.done:
            py.time.Clock().tick(10)
            self.event_loop()
            self.update()
            self.draw()
            py.display.update()
        py.quit()


game = Game(states, "MENU")
game.run()
