import pygame

#KI_Anfang;
    #benutzte KI: Chat Gpt
    # Prompt: Ich muss mein table auf dem Attic haben

def Attic(screen: pygame.Surface):

    attic = pygame.image.load("assets/Bilder/Attic.Topdown.png").convert()

    attic = pygame.transform.scale(attic, (1080, 720))

    sheet = pygame.image.load("assets/Sprites/Indoor/Tilesheets/rogueLikeIndoor_transparent.png").convert_alpha()

    table = sheet.subsurface((101, 152, 18, 35))

    table = pygame.transform.scale_by(table, 5)

    screen.blit(attic, (0, 0))

    screen.blit(table, (800, 320))

#Ki_Ende
