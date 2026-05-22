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

    player = pygame.image.load("assets/Sprites/Characters/Male person/Player.TopDown.png").convert_alpha()

    player = pygame.transform.scale(player, (512, 512))

    player = player.subsurface((56, 40, 67, 122))

    screen.blit(attic, (0, 0))

    screen.blit(table, (800, 320))

    screen.blit(player, (200, 300))

#Ki_Ende
