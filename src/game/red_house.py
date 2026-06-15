import pygame
from src.Game_Variables.game_variables import GameVariables as GV
from src.Game_Variables.game_variables import GameScreens
from src.Game_Variables.game_variables import GameObject
from src.Game_Variables.save_system import save_game
from src.Game_Variables.save_system import load_game
from src.game.player import Player
from src.game.pause_screen import pause_screen
from src.game.sprites import Tilemap
from src.game.medieval_screen import build_map_surface

def red_house(screen: pygame.Surface, clock: pygame.time.Clock, load_save = False):
    GV.init()
    pygame.display.set_caption("Red House")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    player = Player()
    save_message_timer = 0
    if load_save:
        load_game(player)
    paused = False
    image_rect = pygame.Rect(0, 0, 16, 16)
    tilemap = Tilemap("assets/Sprites/Indoor/Tilesheets/roguelikeIndoor_transparent.png",
                      (27, 18), image_rect)
    tilemap= tilemap.load_spritesheet()
    house_map = [
        [()]
    ]

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
        obstacles = []
        player.draw(screen)
        player.move(obstacles=obstacles)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
