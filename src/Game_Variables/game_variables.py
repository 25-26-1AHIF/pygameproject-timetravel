import pygame
from pygame import SRCALPHA


class GameVariables:
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    SQUARE_SIZE = 156
    FPS = 60

    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font = None
    FONT_SMALL: pygame.font.Font = None
    FONT_BUTTONS: pygame.font.Font = None
    FONT_MINI: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont("arial", 68, bold=True)
        GameVariables.FONT_MIDDLE = pygame.sysfont.SysFont("arial", 40, bold=False)
        GameVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 24, bold=False)
        GameVariables.FONT_BUTTONS = pygame.sysfont.SysFont("arial", 34, bold=False)
        GameVariables.FONT_MINI = pygame.sysfont.SysFont("arial", 14, bold=False)

class GameScreens:
    MAIN = "main"
    PLAY = "play"
    EXIT = "exit"
    LADEN = "laden"
    MEDIEVAL = "medieval"
    actual = MAIN

class GameObject:
    def __init__(self, tilemap, object_map, x, y, scale_h, scale_w, tile_width=16, tile_height=16):
        self.object_map = object_map
        self.x = x
        self.y = y
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.scale_h = scale_h
        self.scale_w = scale_w
        self.tilemap = tilemap
        self.image = self.get_image()
        self.rect = self.image.get_rect(topleft=(x, y))

    def get_image(self):
        rows = len(self.object_map)
        cols = len(self.object_map[0])
        obj_surface = pygame.Surface((cols * self.tile_width, rows * self.tile_height), SRCALPHA)

        for row in range(rows):
            for col in range(cols):
                row_tilemap, col_tilemap = self.object_map[row][col]
                tile_bild = self.tilemap[row_tilemap][col_tilemap]

                obj_surface.blit(tile_bild, (col * self.tile_width, row * self.tile_height))

        return obj_surface

    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (self.scale_w,self.scale_h))
        screen.blit(self.image, (self.x, self.y))
