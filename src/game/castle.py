import pygame
from src.Game_Variables.game_variables import GameVariables as GV
from src.Game_Variables.game_variables import GameScreens
from src.Game_Variables.game_variables import GameObject
from src.Game_Variables.save_system import save_game
from src.Game_Variables.save_system import load_game
from src.game.player import Player
from src.game.pause_screen import pause_screen
from src.game.sprites import Tilemap

def castle(screen: pygame.Surface, clock: pygame.time.Clock, load_save = False):
    GV.init()
    pygame.display.set_caption("Red House")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()

    image_rect = pygame.Rect(0,0,32,32)
    tilemap_castle_indoor = Tilemap("assets/Sprites/Indoor/castle.png", (8,19), image_rect)
    tilemap_castle_indoor = tilemap_castle_indoor.load_spritesheet()

    image_ui_rect = pygame.Rect(0, 0, 33, 33)
    tilemap_ui = Tilemap("assets/Sprites/UI_Pack/Tilesheets/Large tiles/Thin outline/tilemap.png", (13, 7),
                         image_ui_rect)
    tilemap_ui = tilemap_ui.load_spritesheet()

    image_ui_small_rect = pygame.Rect(0, 0, 17, 17)
    tilemap_ui_small = Tilemap("assets/Sprites/UI_Pack/Tilesheets/Small tiles/Thin outline/tilemap.png", (23, 7),
                               image_ui_small_rect)
    tilemap_ui_small = tilemap_ui_small.load_spritesheet()

    crown_obj = pygame.image.load("assets/Bilder/Crown_Obj.png").convert_alpha()
    crown_obj = pygame.transform.scale(crown_obj, (50,50))
    player = Player(GV.SCREEN_WIDTH // 2 - GV.PLAYER_WIDTH // 2, 600)
    save_message_timer = 0
    if load_save:
        load_game(player)
    paused = False
    ausgang_rect = pygame.Rect(GV.SCREEN_WIDTH // 2 - 75, GV.SCREEN_HEIGHT - 75, 200, 100)
    crown_rect = pygame.Rect(GV.SCREEN_WIDTH/2-115, 100, 50, 50)
    interactables = [
        {"rect": ausgang_rect, "action": "ausgang"},
        {"rect": crown_rect, "action":"crown"}
    ]
    font = pygame.font.SysFont("Georgia", 32)
    font_mini = pygame.font.SysFont("Georgia", 16)
    crown_found_text = font_mini.render("Congrats! You found the Kings Crown!", True, "black")
    lets_go_rect = pygame.Rect(GV.SCREEN_WIDTH / 2 - 75, GV.SCREEN_HEIGHT / 2 + 20, 75, 150)
    if not GV.SHIELD_IN_INVENTORY and not GV.CANDLE_IN_INVENTORY:
        missing_items_text = font_mini.render("You still have to find the Candle and the Shield", True, "black")
    elif not GV.SHIELD_IN_INVENTORY:
        missing_items_text = font_mini.render("You still have to find the Shield", True, "black")
    elif not GV.CANDLE_IN_INVENTORY:
        missing_items_text = font_mini.render("You still have to find the Candle", True, "black")
    else:
        missing_items_text = font_mini.render("You found all the items, you can go through the portal now!", True, "black")
    text = font.render("Press E to interact", True, (255, 255, 255))
    lets_go_text = font_mini.render("Let's Go!", True, "black")

    map = [
        [(1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,2), (2,3), (2,4), (2,4), (2,4), (2,4), (2,4), (2,4), (2,5),
         (1,0), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1)],
        [(2,0), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1), (2,2), (3,1), (3,1), (3,1), (3,1), (3,1), (3,1), (3,1), (3,1),
         (2,0), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1)],
        [(2,0), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1), (2,2), (0,5), (0,5), (0,5), (0,5), (0,5), (0,5), (0,5), (0,5),
         (2,0), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1)],
        [(2,0), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1), (2,2), (0,5), (0,5), (0,5), (0,5), (0,5), (0,5), (0,5), (0,5),
         (2,0), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1), (2,1)],
        [(3,0), (3,1), (3,1), (3,1), (3,1), (3,1), (3,1), (3,2), (6,4), (6,4), (6,4), (5,4), (5,4), (6,4), (6,4), (6,4),
         (3,0), (3,1), (3,1), (3,1), (3,1), (3,1), (3,1), (3,1)],
        [(0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3),
         (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3), (0,3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)],
        [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
         (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3)]
    ]
    map_obj =GameObject(tilemap_castle_indoor, map, 0,0, GV.SCREEN_HEIGHT, GV.SCREEN_WIDTH, 32, 32)

    window_map = [
        [(15,4)],
        [(16,4)]
    ]
    window_obj = GameObject(tilemap_castle_indoor, window_map, 50, 50, 100, 50, 32,32)
    window_obj2 = GameObject(tilemap_castle_indoor, window_map, 150, 50, 100, 50, 32,32)
    window_obj3 = GameObject(tilemap_castle_indoor, window_map, GV.SCREEN_WIDTH-200, 50, 100, 50, 32,32)
    window_obj4 = GameObject(tilemap_castle_indoor, window_map, GV.SCREEN_WIDTH-100, 50, 100, 50, 32,32)

    pillar_map = [
        [(3,7)],
        [(4,7)],
        [(4,7)],
        [(4,7)],
        [(4,7)],
        [(4,7)],
        [(4,7)],
        [(4,7)],
        [(5,7)]
    ]
    pillar_obj = GameObject(tilemap_castle_indoor, pillar_map, 325, 0, 300, 50, 32, 32)
    pillar_obj2 = GameObject(tilemap_castle_indoor, pillar_map, 700, 0, 300, 50, 32, 32)

    carpet_map = [
        [(4,0), (4,1), (4,2)],
        [(5,0), (5,1), (5,2)],
        [(6,0), (6,1), (6,2)]
    ]

    carpet_obj = GameObject(tilemap_castle_indoor, carpet_map, 490, 90, 100,100, 32,32)

    carpet_long_map = [
        [(4,0), (4,1), (4,2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(5, 0), (5, 1), (5, 2)],
        [(6, 0), (6, 1), (6, 2)]
    ]
    carpet_long_obj = GameObject(tilemap_castle_indoor, carpet_long_map, 440, 250, 500, 200, 32, 32)

    fireplace_map = [
        [(7,5), (7,6), (7,7)],
        [(8,5), (8,6), (8,7)],
        [(9,5), (9,6), (9,7)]
    ]
    fireplace_obj =GameObject(tilemap_castle_indoor, fireplace_map, GV.SCREEN_WIDTH/2-65, 10, 100, 130, 32, 32)

    throne_map = [
        [(13,7)],
        [(14,7)]
    ]
    throne_obj = GameObject(tilemap_castle_indoor, throne_map, GV.SCREEN_WIDTH/2-25, 60, 100, 50, 32, 32)

    sofa_map = [
        [(13,5), (13,6)],
        [(14,5), (14,6)]
    ]
    sofa_obj = GameObject(tilemap_castle_indoor, sofa_map, 50, 200, 100, 150, 32,32)
    sofa_obj2 = GameObject(tilemap_castle_indoor, sofa_map, GV.SCREEN_WIDTH-200, 200, 100, 150, 32 ,32)

    foot_sofa_map = [
        [(15,5)]
    ]
    foot_sofa_obj = GameObject(tilemap_castle_indoor, foot_sofa_map, 0, 290, 50, 50, 32,32)
    sofa_for_crown_obj = GameObject(tilemap_castle_indoor, foot_sofa_map, GV.SCREEN_WIDTH/2-130, 110, 80, 80,32, 32)

    standing_candle_map = [
        [(14,2)],
        [(15,2)],
        [(16,2)]
    ]
    standing_candle_obj = GameObject(tilemap_castle_indoor, standing_candle_map, 0, 200, 100, 50, 32, 32)

    banner_crown_found_map = [
        [(4,4),(4,5),(4,6)]
    ]
    banner_crown_found_obj = GameObject(tilemap_ui, banner_crown_found_map,  GV.SCREEN_WIDTH/2 - 200, GV.SCREEN_HEIGHT/2 - 100, 200, 400, 32, 32)

    button_map = [
        [(2, 3)]
    ]
    button_obj = GameObject(tilemap_ui_small, button_map, GV.SCREEN_WIDTH / 2 - 75, GV.SCREEN_HEIGHT / 2 + 20, 75, 150,16, 16)

    wall_top_left_rect = pygame.Rect(0,0,350,150)
    wall_top_right_rect = pygame.Rect(725,0,350,150)
    sitzecke_links = pygame.Rect(0,200,200,50)

    crown_picked_up = False
    for x in GV.PLAYER_INVENTORY["inventory"]:
        if x == "crown":
            crown_picked_up = True

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
                    if action == "ausgang":
                        return GameScreens.MEDIEVAL
                    if action == "crown":
                        GV.CROWN_IN_INVENTORY = True
                        crown_picked_up = True
                        GV.PLAYER_INVENTORY["inventory"].append("crown")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lets_go_rect.collidepoint(event.pos):
                    GV.FOUND_CROWN_BUTTON_PRESSED = True
        if paused:
            pause_screen(screen, save_message_timer, pause_bild)
            if save_message_timer > 0:
                save_message_timer -= 1
            clock.tick(60)
            continue
        action = player.interact(interactables)

        screen.fill("black")
        map_obj.draw(screen)
        pillar_obj.draw(screen)
        pillar_obj2.draw(screen)
        carpet_obj.draw(screen)
        carpet_long_obj.draw(screen)
        fireplace_obj.draw(screen)
        window_obj.draw(screen)
        window_obj2.draw(screen)
        window_obj3.draw(screen)
        window_obj4.draw(screen)
        throne_obj.draw(screen)
        sofa_obj.draw(screen)
        sofa_obj2.draw(screen)
        standing_candle_obj.draw(screen)
        foot_sofa_obj.draw(screen)
        sofa_for_crown_obj.draw(screen)
        if not crown_picked_up:
            screen.blit(crown_obj, (GV.SCREEN_WIDTH/2-115, 100))
        obstacles = [wall_top_left_rect, wall_top_right_rect, sitzecke_links]
        player.draw(screen)
        if not GV.FOUND_CROWN_BUTTON_PRESSED:
            if GV.CROWN_IN_INVENTORY:
                banner_crown_found_obj.draw(screen)
                screen.blit(crown_found_text, (GV.SCREEN_WIDTH/2 - 130, GV.SCREEN_HEIGHT/2-50))
                screen.blit(missing_items_text, ((GV.SCREEN_WIDTH/2 - 160, GV.SCREEN_HEIGHT/2-20)))
                button_obj.draw(screen)
                screen.blit(lets_go_text, (GV.SCREEN_WIDTH/2-30, GV.SCREEN_HEIGHT/2+50))
        player.move(obstacles=obstacles)
        if action == "ausgang":
            screen.blit(text, (player.x - 150, player.y))
        elif action == "crown" and not crown_picked_up:
            screen.blit(text, (player.x - 150, player.y))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()