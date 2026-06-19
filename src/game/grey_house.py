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

def grey_house(screen: pygame.Surface, clock: pygame.time.Clock, load_save=False):
    GV.init()
    pygame.display.set_caption("Grey House")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    parkett = pygame.image.load("assets/Sprites/Indoor/Parkett_boden.png")
    parkett_boden = pygame.Surface((10 * 32, 10 * 32), SRCALPHA)
    for x in range(10):
        for y in range(10):
            parkett_boden.blit(parkett, (x * 32, y * 32))
    parkett_boden_scaled = pygame.transform.scale(parkett_boden, (GV.SCREEN_WIDTH - 300, GV.SCREEN_HEIGHT - 300))
    player = Player(GV.SCREEN_WIDTH // 2 - GV.PLAYER_WIDTH // 2, 600)
    save_message_timer = 0
    if load_save:
        load_game(player)
    paused = False
    image_rect = pygame.Rect(0, 0, 17, 17)
    tilemap = Tilemap("assets/Sprites/Indoor/Tilesheets/roguelikeIndoor_transparent.png",
                      (27, 18), image_rect)
    tilemap = tilemap.load_spritesheet()

    chest_closed = pygame.image.load("assets/Bilder/Chest_closed.png").convert_alpha()
    chest_closed = pygame.transform.scale(chest_closed, (100,100))
    chest_closed_rect = pygame.Rect(750, 150, 150, 150)

    chest_open = pygame.image.load("assets/Bilder/Chest_open.png").convert_alpha()
    chest_open = pygame.transform.scale(chest_open, (500, 500))
    chest_open_rect = pygame.Rect(GV.SCREEN_WIDTH//2 - 250, GV.SCREEN_HEIGHT//2 - 250, 500, 500)

    wand_oben = [
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (5, 24), (5, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (5, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
    ]

    wand_unten = [
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (1, 7), (1, 7), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (1, 7), (1, 7), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (1, 7), (1, 7), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
        [(4, 26), (5, 23), (6, 24), (6, 24), (6, 24), (6, 24), (6, 24), (1, 7), (1, 7), (6, 24), (6, 24), (6, 24),
         (6, 24), (6, 24), (5, 25), (4, 26)],
    ]
    wand_obj = GameObject(tilemap, wand_oben, GV.SCREEN_WIDTH // 2 - (GV.SCREEN_WIDTH - 300) // 2, 75, 125,
                          GV.SCREEN_WIDTH - 300)
    wand_rect = pygame.Rect(GV.SCREEN_WIDTH // 2 - (GV.SCREEN_WIDTH - 300) // 2, 75, GV.SCREEN_WIDTH - 300, 75)

    wand_rechts = [
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
        [(4, 26)],
    ]
    wand_rechts_obj = GameObject(tilemap, wand_rechts, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 50, 200,
                                 GV.SCREEN_HEIGHT - 350, 50)
    wand_rechts_rect = wand_rechts_obj.rect
    wand_links_obj = GameObject(tilemap, wand_rechts, GV.SCREEN_WIDTH // 2 - (GV.SCREEN_WIDTH - 300) // 2, 200,
                                GV.SCREEN_HEIGHT - 350, 50)
    wand_links_rect = wand_links_obj.rect
    wand_unten_obj = GameObject(tilemap, wand_unten, GV.SCREEN_WIDTH // 2 - (GV.SCREEN_WIDTH - 300) // 2, 445, 125,
                                GV.SCREEN_WIDTH - 300)
    wand_unten_links_rect = pygame.Rect(
        (wand_unten_obj.x, wand_unten_obj.y + 100, (GV.SCREEN_WIDTH - 300) / 2 - 75, 25))
    wand_unten_rechts_rect = pygame.Rect(
        (GV.SCREEN_WIDTH // 2 + 75, wand_unten_obj.y + 100, (GV.SCREEN_WIDTH - 300) / 2 + 75, 25))

    bett_map = [
        [(1, 9), (0, 8)]
    ]
    bett_obj = GameObject(tilemap, bett_map, GV.SCREEN_WIDTH // 2 - (GV.SCREEN_WIDTH - 300) // 2 + 55, 250, 50, 100)

    tisch_map = [
        [(8, 16), (8, 17), (8, 18)]
    ]
    tisch_obj = GameObject(tilemap, tisch_map, GV.SCREEN_WIDTH // 2 - 50, 175, 50, 100)

    wand_teppich_map = [
        [(14, 16), (14, 17), (14, 18)]
    ]
    wand_teppich_onj = GameObject(tilemap, wand_teppich_map, GV.SCREEN_WIDTH // 2 - 50, 125, 50, 100)

    bank_map = [
        [(11, 26)],
        [(12, 26)]
    ]
    bank_obj = GameObject(tilemap, bank_map, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 100, 300, 100, 50)

    ess_tisch_map = [
        [(9, 5)],
        [(10, 5)],
        [(11, 5)],
    ]
    ess_tisch_obj = GameObject(tilemap, ess_tisch_map, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 150, 300,
                               100, 50)

    stuhl_map = [
        [(6, 2)]
    ]

    stuhl_map2 = [
        [(6, 1)]
    ]

    stuhl_map3 = [
        [(6, 0)]
    ]

    stuhl_obj = GameObject(tilemap, stuhl_map, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 180, 300, 50, 50)
    stuhl_obj2 = GameObject(tilemap, stuhl_map, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 180, 340, 50, 50)
    stuhl_obj3 = GameObject(tilemap, stuhl_map2, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 150, 380, 50, 50)
    stuhl_obj4 = GameObject(tilemap, stuhl_map3, GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 150, 280, 50, 50)

    ess_ecke_rect = pygame.Rect(GV.SCREEN_WIDTH // 2 + (GV.SCREEN_WIDTH - 300) // 2 - 180, 310, 150, 90)

    shield_map = [
        [(10,22)]
    ]

    shield_obj = GameObject(tilemap, shield_map, GV.SCREEN_WIDTH//2 - 50, GV.SCREEN_HEIGHT//2 - 75, 100, 100)
    shield_rect = pygame.Rect(GV.SCREEN_WIDTH//2 - 25, GV.SCREEN_HEIGHT//2 - 75, 50, 75)

    portrait_map = [
        [(15, 20)],
        [(16, 20)]
    ]
    portrait_obj = GameObject(tilemap, portrait_map, 300, 100, 100, 50)

    ausgang_rect = pygame.Rect(GV.SCREEN_WIDTH // 2 - 75, GV.SCREEN_HEIGHT - 75, 150, 75)

    interactables = [
        {"rect": ausgang_rect, "action": "ausgang"},
        {"rect": chest_closed_rect, "action": "chest_open"}
    ]
    font = pygame.font.SysFont("Georgia", 32)
    text = font.render("Press E to interact", True, (255, 255, 255))
    chest = False
    shield = True
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
                    if action == "chest_open":
                        chest = not chest
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shield_rect.collidepoint(event.pos):
                    shield = False
        if paused:
            pause_screen(screen, save_message_timer, pause_bild)
            if save_message_timer > 0:
                save_message_timer -= 1
            clock.tick(60)
            continue
        screen.fill("black")
        screen.blit(parkett_boden_scaled, (GV.SCREEN_WIDTH // 2 - (GV.SCREEN_WIDTH - 300) // 2,
                                           GV.SCREEN_HEIGHT // 2 - (GV.SCREEN_HEIGHT - 300) // 2))
        obstacles = [wand_rect, wand_rechts_rect, wand_links_rect, wand_unten_links_rect, wand_unten_rechts_rect, ess_ecke_rect]
        wand_obj.draw(screen)
        wand_links_obj.draw(screen)
        wand_rechts_obj.draw(screen)
        bett_obj.draw(screen)
        tisch_obj.draw(screen)
        wand_teppich_onj.draw(screen)
        bank_obj.draw(screen)
        stuhl_obj.draw(screen)
        stuhl_obj2.draw(screen)
        stuhl_obj4.draw(screen)
        ess_tisch_obj.draw(screen)
        stuhl_obj3.draw(screen)
        portrait_obj.draw(screen)
        if not chest:
            screen.blit(chest_closed, chest_closed_rect)
        player.draw(screen)
        action = player.interact(interactables)
        if action == "ausgang":
            screen.blit(text, (player.x - 150, player.y))
        if action == "chest_open":
            screen.blit(text, (player.x - 150, player.y))
        wand_unten_obj.draw(screen)
        if chest:
            screen.blit(chest_open, chest_open_rect)
            if shield:
                shield_obj.draw(screen)
        player.move(obstacles=obstacles)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()