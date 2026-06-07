import pygame
from src.Game_Variables.game_variables import GameVariables as GV
from src.Game_Variables.game_variables import GameScreens
from src.Game_Variables.game_variables import GameObject
from src.Game_Variables.save_system import save_game
from src.Game_Variables.save_system import load_game
from src.game.player import Player
from src.game.pause_screen import pause_screen
from src.game.sprites import Tilemap

def medieval_screen(screen: pygame.Surface, clock: pygame.time.Clock, load_save=False):
    GV.init()
    pygame.display.set_caption("Medieval_Screen")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    player = Player()
    save_message_timer = 0
    if load_save:
        load_game(player)
    paused = False
    image_rect = pygame.Rect(0, 0, 16, 16)
    tilemap = Tilemap("assets/Sprites/Town (medieval)/Tilemap/tilemap_packed.png",
                      (12, 11), image_rect)
    tilemap = tilemap.load_spritesheet()
    house_map = [
        [(4,0), (4,1), (4,3), (4,2)],
        [(5,0), (5,3), (5,1), (5,2)],
        [(6,0), (7,0), (7,1), (6,3)],
    ]
    house_object = GameObject(tilemap, house_map, 100,0, 400, 500)

    well_map = [
                [(7,8)],
                [(8,8)]
    ]
    well_obj = GameObject(tilemap, well_map, 600, 100, 200, 100)

    level_map = [
        [(0,0), (0,0), (0,0), (0,0), (0,2), (2,0), (2,2), (0,0)],
        [(0,0), (0,0), (0,0), (0,0), (0,0), (2,0), (2,2), (0,0)],
        [(0,0), (0,0), (0,0), (0,0), (0,2), (2,0), (2,2), (0,0)],
        [(0,1), (0,2), (3,3), (0,2), (0,0), (2,0), (2,2), (0,0)],
        [(0,1), (0,2), (3,6), (1,2), (0,0), (2,0), (2,2), (0,0)],
        [(0,1), (0,2), (2,0), (2,2), (0,0), (2,0), (2,2), (0,0)],
        [(0,1), (0,2), (2,0), (2,2), (0,0), (2,0), (2,2), (0,0)],
        [(0,1), (0,2), (2,0), (3,4), (1,1), (3,3), (2,2), (0,0)],
        [(0,1), (0,2), (3,0), (3,1), (3,1), (3,1), (2,2), (0,0)],
    ]
    map_surface = build_map_surface(tilemap, level_map)
    scaled_map = pygame.transform.scale(map_surface, (1080, 720))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                if paused and event.key == pygame.K_s:
                    save_game(player)
                    save_message_timer = 120
                if paused and event.key == pygame.K_m:
                    return GameScreens.MAIN
                if paused and event.key == pygame.K_q:
                    return None
        if paused:
            pause_screen(screen,save_message_timer,pause_bild)
            if save_message_timer > 0:
                save_message_timer -= 1
            clock.tick(60)
            continue
        screen.fill("black")
        screen.blit(scaled_map, (0, 0))
        house_object.draw(screen)
        well_obj.draw(screen)
        player.draw(screen)
        player.move(obstacles=0)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# KI-Anfang
# benutzte KI: Microsoft Copilot
# Prompt: <Code> Wie kann ich da eine Map erstellen wie ich will? Erklär es mir bitte.
# WICHTIG! Nur Grundskelett mit KI generiert. Diese Form wurde abgeändert und ist nicht rein KI!
def build_map_surface(tilemap, level_map, tile_w=16, tile_h=16):
    rows = len(level_map)
    cols = len(level_map[0])

    # Surface für die ganze Map
    map_surface = pygame.Surface((cols * tile_w, rows * tile_h))

    for row in range(rows):
        for col in range(cols):
            row_tilemap, col_tilemap = level_map[row][col]
            tile_bild = tilemap[row_tilemap][col_tilemap]

            map_surface.blit(tile_bild, (col * tile_w, row * tile_h))

    return map_surface
# KI-Ende