import pygame

def Attic(screen: pygame.Surface):

    attic = pygame.image.load("assets/Bilder/Attic.Topdown.png").convert()

    attic = pygame.transform.scale(attic, (1080, 720))

    sheet = pygame.image.load("assets/Sprites/Indoor/Tilesheets/rogueLikeIndoor_transparent.png").convert_alpha()

    table = sheet.subsurface((101, 152, 18, 35))

    table = pygame.transform.scale(table, (80, 150))

    table_rect = table.get_rect(topleft=(800, 350))
    screen.blit(attic, (0, 0))
    screen.blit(table, (800, 350))

    return table_rect