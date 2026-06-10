# Color
import pygame

COLOR_MENU = (10, 104, 196)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 228, 65)

# Options Menu
MENU_OPTION = ('NEW GAME SINGLE-PLAYER',
               'NEW GAME COOPERATIVE',
               'SCORE',
               'EXIT')
# Windows
WIN_WIDTH = 576#943
WIN_HEIGHT = 324#577


EVENT_ENEMY = pygame.USEREVENT + 1
# Speed
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 4,
    'Player1': 4,
    'Enemy1' : 3,
    'Enemy2' : 3,
}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Enemy1' : 50,
    'Enemy2' : 50,
}


#S
SPAWN_TIME = 4000