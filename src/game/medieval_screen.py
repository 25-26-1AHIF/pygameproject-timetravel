from calendar import leapdays

import pygame
from src.Game_Variables.game_variables import GameVariables as GV
from src.Game_Variables.game_variables import GameScreens
from src.Game_Variables.game_variables import GameObject
from src.Game_Variables.save_system import save_game
from src.Game_Variables.save_system import load_game
from src.game.player import Player
from src.game.pause_screen import pause_screen
from src.game.sprites import Tilemap
from src.game.leaderboard import Leaderboard

def medieval_screen(screen: pygame.Surface, clock: pygame.time.Clock, load_save=False):
    GV.init()
    if not GV.STARTED_TIME:
        GV.START_TIME = pygame.time.get_ticks()
        GV.STARTED_TIME = True
    pygame.display.set_caption("Medieval_Screen")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    kerze_bild_sw = pygame.image.load("assets/Bilder/Kerze_schwarz_weiß.png").convert_alpha()
    kerze_bild_bunt = pygame.image.load("assets/Bilder/Kerze_bunt.png").convert_alpha()
    shield_image_sw = pygame.image.load("assets/Bilder/Schild_Schwarz_weiß.png").convert_alpha()
    shield_image_bunt = pygame.image.load("assets/Bilder/Schild_bunt.png").convert_alpha()
    crown_image_sw = pygame.image.load("assets/Bilder/Krone_Schwarz_weiß.png").convert_alpha()
    crown_image_bunt = pygame.image.load("assets/Bilder/Krone_bunt.png").convert_alpha()
    crown_image_sw = pygame.transform.scale(crown_image_sw, (100,100))
    crown_image_bunt = pygame.transform.scale(crown_image_bunt, (100, 100))
    shield_image_sw = pygame.transform.scale(shield_image_sw, (100,100))
    shield_image_bunt = pygame.transform.scale(shield_image_bunt, (100,100))
    kerze_bild_sw = pygame.transform.scale(kerze_bild_sw, (100, 100))
    kerze_bild_bunt = pygame.transform.scale(kerze_bild_bunt, (100, 100))
    portal_bild = pygame.image.load("assets/Bilder/Portal_medieval.png").convert_alpha()
    portal_bild = pygame.transform.scale(portal_bild, (200, 200))
    player = Player()
    save_message_timer = 0
    if load_save:
        load_game(player)
    paused = False
    image_rect = pygame.Rect(0, 0, 16, 16)
    tilemap = Tilemap("assets/Sprites/Town (medieval)/Tilemap/tilemap_packed.png",
                      (12, 11), image_rect)
    tilemap = tilemap.load_spritesheet()

    image_ui_rect = pygame.Rect(0,0, 33, 33)
    tilemap_ui = Tilemap("assets/Sprites/UI_Pack/Tilesheets/Large tiles/Thin outline/tilemap.png", (13,7), image_ui_rect)
    tilemap_ui = tilemap_ui.load_spritesheet()

    image_ui_small_rect = pygame.Rect(0,0,17,17)
    tilemap_ui_small = Tilemap("assets/Sprites/UI_Pack/Tilesheets/Small tiles/Thin outline/tilemap.png", (23,7), image_ui_small_rect)
    tilemap_ui_small = tilemap_ui_small.load_spritesheet()

    banner_welcome_map = [
        [(4,4),(4,5),(4,6)]
    ]
    banner_welcome_obj = GameObject(tilemap_ui, banner_welcome_map,  GV.SCREEN_WIDTH/2 - 175, GV.SCREEN_HEIGHT/2 - 100, 150, 350, 32, 32)

    button_map = [
        [(2,3)]
    ]
    button_obj = GameObject(tilemap_ui_small, button_map, GV.SCREEN_WIDTH/2 - 70, GV.SCREEN_HEIGHT/2 - 10, 75, 130, 16, 16)

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

    portal_medieval_pos = (900, 500, 170, 170)
    portal_rect = pygame.Rect(portal_medieval_pos[0], portal_medieval_pos[1], 80, 100)

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
        {"rect": castle_door, "action": "castle"},
        {"rect": portal_medieval_pos, "action": "portal"}
    ]
    font = pygame.font.SysFont("Georgia", 32)
    text = font.render("Press E to interact", True, (255, 255, 255))
    font_mini = pygame.font.SysFont("Georgia", 18)
    text_welcome = font_mini.render("Collect all 3 Objects shown ", True, "black")
    text_welcome2 = font_mini.render("Top-Left to go back to the present!", True, "black")
    got_it_text = font_mini.render("Got it!", True, "black")

    text_quiz_object_not_collected = font.render(f"Collect Quest-Objects first Brudi", True, (255, 0, 0))

    got_it_rect = pygame.Rect((GV.SCREEN_WIDTH/2 - 70, GV.SCREEN_HEIGHT/2 - 10, 75, 130))

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
                    if action == "portal" and GV.GOT_ALL_ITEMS:
                        return GameScreens.LEADERBOARD
            if event.type == pygame.MOUSEBUTTONDOWN:
                if got_it_rect.collidepoint(event.pos):
                    GV.GOT_IT_WELCOME = True
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
        screen.blit(portal_bild, portal_medieval_pos)
        player.draw(screen)
        if not GV.GOT_IT_WELCOME:
            banner_welcome_obj.draw(screen)
            screen.blit(text_welcome, (GV.SCREEN_WIDTH/2 - 100, GV.SCREEN_HEIGHT/2-50))
            screen.blit(text_welcome2, ((GV.SCREEN_WIDTH/2 - 140, GV.SCREEN_HEIGHT/2-30)))
            button_obj.draw(screen)
            screen.blit(got_it_text, (GV.SCREEN_WIDTH/2-30, GV.SCREEN_HEIGHT/2+15))

        if GV.CANDLE_IN_INVENTORY:
            screen.blit(kerze_bild_bunt, (0,0))
        else:
            screen.blit(kerze_bild_sw, (0,0))

        if GV.SHIELD_IN_INVENTORY:
            screen.blit(shield_image_bunt, (90, 0))
        else:
            screen.blit(shield_image_sw, (90, 0))

        if GV.CROWN_IN_INVENTORY:
            screen.blit(crown_image_bunt, (180,0))
        else:
            screen.blit(crown_image_sw, (180, 0))

        if GV.GOT_ALL_ITEMS and GV.STARTED_TIME:
            # KI-Anfang:
            # Benutzte KI: Microsoft Copilot
            # URL: https://copilot.microsoft.com
            # Prompt: Ich will, damit mein Spiel kompetitiver wird,
            # die Zeit messen, die der Player braucht um alle drei Objekte zu finden.
            # Wie kann ich das machen, weil ich habe ja 60 FPS und wie mach ich das jetzt? Am Ende des Spiels will ich noch so,
            # dass der Player seinen Namen eingibt und es dann ein Leaderboard gibt mit Name und Zeit.
            end_time = pygame.time.get_ticks()
            GV.END_TIME = end_time
            print(GV.END_TIME, GV.START_TIME)
            GV.FINAL_TIME = (GV.END_TIME - GV.START_TIME) / 1000
            print(GV.FINAL_TIME)

            #KI-Ende
        wand_links = pygame.Rect((0,0,5,GV.SCREEN_HEIGHT))
        wand_rechts = pygame.Rect((GV.SCREEN_WIDTH -5,0,5,GV.SCREEN_HEIGHT))
        wand_oben = pygame.Rect((0,0,GV.SCREEN_WIDTH,5))
        wand_unten = pygame.Rect((0, GV.SCREEN_HEIGHT -5, GV.SCREEN_WIDTH, 5))
        obstacles = [house_red_rect,house_grey_rect,castle_rect,
                     wand_links, brunnen_rect,
                     wand_rechts, wand_oben, wand_unten]
        action = player.interact(interactables)
        if action == "portal":
            if not GV.SHIELD_IN_INVENTORY or not GV.CANDLE_IN_INVENTORY or not GV.CROWN_IN_INVENTORY:
                screen.blit(text_quiz_object_not_collected, (player.x - 250, player.y - 40))
            else:
                GV.GOT_ALL_ITEMS = True
                screen.blit(text, (player.x - 150, player.y - 40))
        elif action:
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
