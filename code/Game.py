#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Lose import Lose
from code.Player import Player
from code.Victory import Victory
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, EVENT_TIMEOUT
from code.Level import Level
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            victory = Victory(self.window)
            lose = Lose(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                p_score = [0]
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run(p_score)
                if level_return:
                    victory.run(menu_return)


            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()  # end game
            else:
                pygame.quit()
                sys.exit()
