import pygame
from src.Game_Variables.game_variables import GameVariables as GV

def Attic(screen: pygame.Surface):
    attic = pygame.image.load("assets/Sprites/Attic/Attic.Topdown.png").convert()
    attic = pygame.transform.scale(attic, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    stairs = pygame.image.load("assets/Bilder/Stairs_Attic.png").convert()
    stairs = pygame.transform.scale(stairs, (100, 100))
    stairs_rect = pygame.Rect(210, 300, 50, 20)
    sheet = pygame.image.load("assets/Sprites/Indoor/Tilesheets/rogueLikeIndoor_transparent.png").convert_alpha()
    table_up = sheet.subsurface((102, 153, 16, 17))
    table_down = sheet.subsurface((102, 170, 16, 17))
    diary_closed = pygame.image.load("assets/Sprites/Diary/Diary_geschlossen.png")
    diary_closed = pygame.transform.scale(diary_closed, (60,60))
    mini_font = pygame.font.SysFont("Georgia",10)
    mini_text = mini_font.render("Diary", True, "#f09941")
    mini_text_rect = mini_text.get_rect(center=(827, 460))


    # KI Anfang
    # benutzte KI: Microsoft Copilot
    # Prompt: Das Problem ist jetzt, dass der Tisch jetzt 1pxl Gap hat dazwischen,
    # also der Tisch ist praktisch in 2 Teile geteilt.
    # Kann ich nicht ein Stück rausschneiden, dann das andere,
    # danach das zusammenfügen und es als table zurückgeben?
    table = pygame.Surface((32, 35), pygame.SRCALPHA)
    table.blit(table_up, (0, 0))
    table.blit(table_down, (0, 16))
    # KI Ende

    table = pygame.transform.scale(table, (120, 200))
    table_rect = pygame.Rect(820, 380, 30, 60)
    screen.blit(attic, (0, 0))
    screen.blit(table, (795, 360))
    screen.blit(diary_closed, (785, 440))
    screen.blit(mini_text, mini_text_rect)
    screen.blit(stairs, (180, 300))

    return table_rect, stairs_rect