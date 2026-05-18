import pygame

class GameVariables:
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    SQUARE_SIZE = 156
    FPS = 60

    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font = None
    FONT_SMALL: pygame.font.Font = None
    FONT_BUTTONS: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont("arial", 68, bold=True)
        GameVariables.FONT_MIDDLE = pygame.sysfont.SysFont("arial", 40, bold=False)
        GameVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 24, bold=False)
        GameVariables.FONT_BUTTONS = pygame.sysfont.SysFont("arial", 34, bold=False)

class GameScreens:
    MAIN = "main"
    PLAY = "play"
    EXIT = "exit"
    actual = MAIN