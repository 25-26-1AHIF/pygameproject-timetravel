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
    house_object = GameObject(tilemap, house_map, 95,150, GV.HOUSE_SCALE_H, GV.HOUSE_SCALE_W)
    red_house_door = pygame.Rect(225, 250, 60, 60)

    grey_house_map = [
        [(4, 4), (4, 5), (4, 7), (4, 6)],
        [(5, 4), (5, 7), (5, 5), (5, 6)],
        [(6, 4), (7, 4), (7, 5), (6, 7)],
    ]
    grey_house_object = GameObject(tilemap, grey_house_map, 450,0, GV.HOUSE_SCALE_H, GV.HOUSE_SCALE_W)
    grey_house_door = pygame.Rect(575, 100, 60, 60)

    castle_map = [
        [(8,0), (8,1), (8,2), (8,3), (8,5)],
        [(10,0), (10,1), (10,2), (10,6), (10,6)],
        [(10,6), (9,3), (9,4), (10,6), (10,6)],
        [(10,6), (10,3), (10,4), (10,6), (10,6)],
    ]
    castle_object = GameObject(tilemap, castle_map, 835,150, 300, 200)
    castle_door = pygame.Rect(880, 325, 60, 120)

    brunnen_map = [
        [(7,8)],
        [(8,8)],
    ]

    brunnen_object = GameObject(tilemap, brunnen_map, 400, 380, 150, 75)

    tree1_map = [
        [(0,3)],
        [(1,3)]
    ]
    tree1_obj = GameObject(tilemap, tree1_map, 850, 0, 100, 50)

    house_red_rect = pygame.Rect(110, 150, 220, 95)
    house_grey_rect = pygame.Rect(490, 40, 230, 70)
    castle_rect = pygame.Rect(castle_object.rect.x, castle_object.rect.y,
                              castle_object.rect.height-50, castle_object.rect.width)
    brunnen_rect = pygame.Rect(405, 430, 65, 100)

    level_map = [
        [(0,0), (0,0), (0,0), (0,0), (0,2), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,0), (0,0), (0,0), (0,0), (0,0), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,0), (0,0), (0,0), (0,0), (0,2), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,1), (0,2), (0,1), (0,2), (0,0), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,1), (0,2), (3,6), (0,0), (0,0), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,1), (0,2), (2,0), (0,0), (0,0), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,1), (0,2), (2,0), (0,0), (0,0), (2,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,1), (0,2), (2,0), (1,1), (1,1), (3,3), (0,0), (0,0), (3,7), (0,2)],
        [(0,1), (0,2), (2,0), (2,1), (2,1), (2,1), (0,0), (0,0), (3,7), (0,2)],
        [(0,1), (0,2), (2,0), (2,1), (2,1), (2,1), (0,0), (0,0), (3,7), (0,2)],
        [(0,0), (0,0), (2,0), (2,1), (2,1), (2,1), (3,7), (3,7), (3,7), (0,2)],
        [(0,0), (0,0), (3,0), (3,1), (3,1), (3,2), (0,0), (0,0), (0,1), (0,2)],
        [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1), (0,2)],
        [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1), (0,2)],
    ]

    map_surface = build_map_surface(tilemap, level_map)
    scaled_map = pygame.transform.scale(map_surface, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    interactables = [
        {"rect": grey_house_door, "action": "g_house"},
        {"rect": red_house_door, "action": "r_house"},
        {"rect": castle_door, "action": "castle"}
    ]
    font = pygame.font.SysFont("Georgia", 32)
    text = font.render("Press E to interact", True, (255, 255, 255))
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
                if event.key == pygame.K_e:
                    if action == "g_house":
                        return GameScreens.G_HOUSE
                    if action == "r_house":
                        return GameScreens.R_HOUSE
                    if action == "castle":
                        return GameScreens.CASTLE
        if paused:
            pause_screen(screen,save_message_timer,pause_bild)
            if save_message_timer > 0:
                save_message_timer -= 1
            clock.tick(60)
            continue
        screen.fill("black")
        screen.blit(scaled_map, (0, 0))
        house_object.draw(screen)
        grey_house_object.draw(screen)
        castle_object.draw(screen)
        brunnen_object.draw(screen)
        tree1_obj.draw(screen)
        player.draw(screen)
        quest_text = GV.FONT_MIDDLE.render("Artefakte gefunden: /3", True, "black")
        wand_links = pygame.Rect((0,0,5,GV.SCREEN_HEIGHT))
        wand_rechts = pygame.Rect((GV.SCREEN_WIDTH -5,0,5,GV.SCREEN_HEIGHT))
        wand_oben = pygame.Rect((0,0,GV.SCREEN_WIDTH,5))
        wand_unten = pygame.Rect((0, GV.SCREEN_HEIGHT -5, GV.SCREEN_WIDTH, 5))
        obstacles = [house_red_rect,house_grey_rect,castle_rect,
                     wand_links, brunnen_rect,
                     wand_rechts, wand_oben, wand_unten]
        action = player.interact(interactables)
        if action:
            screen.blit(text, (player.x - 150, player.y - 40))
        player.move(obstacles=obstacles)
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
    map_surface = pygame.Surface((cols * tile_w, rows * tile_h), pygame.SRCALPHA)
    map_surface.fill((0,0,0,0))

    for row in range(rows):
        for col in range(cols):
            row_tilemap, col_tilemap = level_map[row][col]
            tile_bild = tilemap[row_tilemap][col_tilemap]

            map_surface.blit(tile_bild, (col * tile_w, row * tile_h))

    return map_surface
# KI-Ende