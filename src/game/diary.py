from src.Game_Variables.game_variables import GameVariables as GV
import pygame

def diary(screen: pygame.Surface, filepath: str):
    diary_bild = pygame.image.load(filepath).convert()
    #screen.blit(diary_bild, dest=(GV.SCREEN_WIDTH/2 - diary_bild_breite/2, GV.SCREEN_HEIGHT/2 - diary_bild_breite/2))

    #KI_Anfang;
    #benutzte KI: Microsoft Copilot
    # Prompt: Wie kann ich in Pycharm ein Sprite vergrößert darstellen,
    # ohne dass sich die Pixel des Bildes ändern? Geht das?
    # Muss ich dafür ein neues Sprite erstellen?

    scale_factor = 10  # z.B. 4x größer
    width = diary_bild.get_width() * scale_factor
    height = diary_bild.get_height() * scale_factor

    sprite_big = pygame.transform.scale(diary_bild, (width, height))

    screen.blit(sprite_big, dest=(GV.SCREEN_WIDTH/2 - width/2, GV.SCREEN_HEIGHT/2 - height/2))

    # KI-Ende