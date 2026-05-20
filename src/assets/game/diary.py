from src.assets.Game_Variables.game_variables import GameVariables as GV
import pygame

def diary(screen: pygame.Surface):
    diary_bild = pygame.image.load("assets/Sprites/Diary/Diary.png").convert()
    diary_bild_breite = diary_bild.get_width()
    screen.blit(diary_bild, dest=(GV.SCREEN_WIDTH/2 - diary_bild_breite/2, GV.SCREEN_HEIGHT/2 - diary_bild_breite/2))