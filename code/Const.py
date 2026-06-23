# Color
import pygame

COLOR_MENU = (10, 104, 196)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 228, 65)

# Options Menu
MENU_OPTION = ('NEW GAME SINGLE-PLAYER',
               'EXIT')

# Windows
WIN_WIDTH = 576  # 943
WIN_HEIGHT = 324  # 577

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
# Speed
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 8,
    'Level1Bg3': 3,
    'Level1Bg4': 3,
    # 'Level1Bg5': 2,
    # 'Level1Bg6': 7,
    # 'Level1Bg7': 3,
    # 'Level1Bg8': 7,
    'Player1': 4,
    'Player1Shot': 2,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    # 'Level1Bg5': 999,
    # 'Level1Bg6': 999,
    # 'Level1Bg7': 999,
    # 'Level1Bg8': 999,
    'Player1': 3,
    'Player1Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 50,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    # 'Level1Bg5': 2,
    # 'Level1Bg6': 7,
    # 'Level1Bg7': 3,
    # 'Level1Bg8': 7,
    'Player1': 1,
    'Player1Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    # 'Level1Bg5': 2,
    # 'Level1Bg6': 7,
    # 'Level1Bg7': 3,
    # 'Level1Bg8': 7,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 100,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1': 100,
    'Enemy2': 200,

}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    }
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    }

# S
SPAWN_TIME = 600
