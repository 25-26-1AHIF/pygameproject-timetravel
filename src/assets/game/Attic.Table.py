import pygame

def Attic(screen: pygame.Surface):
    Attic_bild = pygame.image.load("assets/Sprites/Indoor/Tilesheets/roguelikeIndoor_transparent.png").convert_alpha()

    Attic_table = Attic_bild.subsurface((101, 152, 18, 35))

    Attic.bild = pygame.transform.scale_by(Attic_table, 10)

    screen.blit(Attic_table, (0, 0))
