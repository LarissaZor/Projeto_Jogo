import sys

import pygame
from pygame import Surface, Rect, KEYDOWN
from pygame.font import Font

from code.Const import COLOR_MENU, WIN_WIDTH, C_WHITE, MENU_OPTION, C_YELLOW


class Victory:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/sky.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def run(self, game_mode: str):
        pygame.image.load("./assets/sky.png").convert_alpha()
        pygame.mixer_music.load('./assets/soundMenu.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.menu_vic(50, 'YOU WIN!!', C_WHITE, ((WIN_WIDTH / 2), 60))
            self.menu_vic(25, 'Retornar ao menu', C_YELLOW, ((WIN_WIDTH / 2), 250))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return
                pygame.display.flip()

    def menu_vic(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Planes_ValMore", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
