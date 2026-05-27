#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_MENU, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/War4/Menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./assets/soundMenu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "One", COLOR_MENU, ((WIN_WIDTH / 5), 200))
            self.menu_text(70, "More", COLOR_MENU, ((WIN_WIDTH / 5), 260))
            self.menu_text(70, "Night", COLOR_MENU, ((WIN_WIDTH / 5), 320))

            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 5), 300 + 10 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quit..")
                    pygame.quit()  # Close window
                    quit()  # end game

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
