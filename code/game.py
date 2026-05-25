#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        # ctrl+alt+l --- organiza o código de acordo com a pep(retira spaces)
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            # # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         print("Quit..")
            #         pygame.quit()  # Close window
            #         quit()
