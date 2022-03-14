import pygame as py
import tools as tl
import config as cfg
import _thread
import network as nt

class Wait(object):
    def __init__(self,run_server):
        self.done = False
        self.next_state = None
        self.button_back = tl.Button(cfg.button_back_image, 0, 0)
        self.run_server = run_server
        self.network = nt.Network()
    def get_event(self, event):

        if self.run_server:
            print("run server!")
            self.network.build_server()
            _thread.start_new_thread(self.network.connection_attempt,(None,))
            self.run_server = False

        if event.type == py.QUIT:
            self.done = True
            sys.exit()

        if self.button_back.pressed(event):
            self.next_state = "LOBBY"

        if self.network.connected():
            print('RECIEVED!')
            print(self.network.conn)

    def draw(self, window):

        window.blit(cfg.background_wait, (0, 0))

        self.button_back.draw(window)
