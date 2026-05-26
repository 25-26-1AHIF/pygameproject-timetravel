import pygame

def player(screen: pygame.Surface):
    player_bild = pygame.image.load("assets/Sprites/Characters//Male person/Charakter.TopDown.png").convert_alpha()

    player_bild = player_bild.subsurface((0, 0, 16, 16))

    player.bild = pygame.transform.scale_by(player_bild, 10)

    screen.blit(player_bild, (0, 0))
