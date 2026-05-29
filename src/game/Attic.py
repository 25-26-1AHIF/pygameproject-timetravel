import pygame

def Attic(screen: pygame.Surface):

    attic = pygame.image.load("assets/Bilder/Attic.Topdown.png").convert()

    attic = pygame.transform.scale(attic, (1080, 720))

    stairs = pygame.image.load("assets/Bilder/Stairs_Attic.png").convert()

    stairs = pygame.transform.scale(stairs, (100, 100))

    stairs_rect = pygame.Rect(210, 300, 50, 20)

    sheet = pygame.image.load("assets/Sprites/Indoor/Tilesheets/rogueLikeIndoor_transparent.png").convert_alpha()

    table = sheet.subsurface((101, 152, 18, 35))

    table = pygame.transform.scale(table, (85, 160))

    table_rect = pygame.Rect(820, 380, 30, 60)

    screen.blit(attic, (0, 0))
    screen.blit(table, (795, 360))
    screen.blit(stairs, (180, 300))

    return table_rect, stairs_rect