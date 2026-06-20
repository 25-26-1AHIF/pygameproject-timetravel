import pygame
from pygame import SRCALPHA
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
    castle_indoor = pygame.image.load("assets/Sprites/Indoor/castle.png").convert_alpha()
    tilemap_castle_indoor = Tilemap("assets/Sprites/Indoor/castle.png", (8,19), image_rect)
    tilemap_castle_indoor = tilemap_castle_indoor.load_spritesheet()
    player = Player(GV.SCREEN_WIDTH // 2 - GV.PLAYER_WIDTH // 2, 600)
    save_message_timer = 0
    if load_save:
        load_game(player)
    paused = False
    ausgang_rect = pygame.Rect(GV.SCREEN_WIDTH // 2 - 75, GV.SCREEN_HEIGHT - 75, 200, 100)
    interactables = [
        {"rect": ausgang_rect, "action": "ausgang"}
    ]
    font = pygame.font.SysFont("Georgia", 32)
    text = font.render("Press E to interact", True, (255, 255, 255))

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
    carpet_long_obj = GameObject(tilemap_castle_indoor, carpet_long_map, 490, 250, 500, 100, 32, 32)

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
        obstacles = []
        player.draw(screen)
        player.move(obstacles=obstacles)
        if action == "ausgang":
            screen.blit(text, (player.x - 150, player.y))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()