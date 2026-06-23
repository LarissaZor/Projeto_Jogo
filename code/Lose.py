import sys

import pygame
from pygame import Surface, Rect, KEYDOWN
from pygame.font import Font

from code.Const import C_YELLOW, WIN_WIDTH, C_WHITE


class Lose:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/sky.png').convert_alpha()
        self.rect = self.surf.get_rect()
        pass

    def run(self):
        pygame.image.load("./assets/sky.png").convert_alpha()
        pygame.mixer_music.load('./assets/soundMenu.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.menu_lose(50, 'YOU LOSE!!', C_WHITE, ((WIN_WIDTH / 2), 60))
            self.menu_lose(25, 'Retornar ao menu', C_YELLOW, ((WIN_WIDTH / 2), 250))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return
                pygame.display.flip()

    def menu_lose(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Planes_ValMore", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
