import pygame
from src.Game_Variables.game_variables import GameScreens
from src.game.player import Player
from src.Game_Variables.game_variables import GameVariables as GV
from src.game.pause_screen import pause_screen
from src.game.Attic import Attic
from src.Game_Variables.save_system import save_game
from src.Game_Variables.save_system import load_game
from src.game.diary import diary as diary_ausfuehren

def play_screen(screen: pygame.Surface, clock: pygame.time.Clock, load_save=False):
    GV.init()
    diary_open = False
    pygame.display.set_caption("TimeTravel - Play-Screen")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    pause_bild = pygame.transform.scale(pause_bild, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    player = Player()
    diary = diary_ausfuehren(screen=screen, filepath="assets/Sprites/Diary/Diary.png")
    medieval_icon = pygame.image.load("assets/Sprites/Icons/Medieval_Icon.png")
    medieval_icon_rect = medieval_icon.get_rect(center=(diary.medievel_icon_pos))
    if load_save:
        load_game(player)
    paused = False
    save_message_timer = 0
    walls = [
        pygame.Rect(90, 185, 900, 20),
        pygame.Rect(90, 670, 900, 20),
        pygame.Rect(90, 185, 20, 500),
        pygame.Rect(970, 185, 20, 500),
    ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if player.interact(screen=screen) and event.key == pygame.K_e:
                    diary_open = not diary_open
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                if paused and event.key == pygame.K_s:
                    save_game(player)
                    save_message_timer = 120
                if paused and event.key == pygame.K_m:
                    return GameScreens.MAIN
                if paused and event.key == pygame.K_q:
                    return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if medieval_icon_rect.collidepoint(event.pos):
                    return GameScreens.MEDIEVAL
        if paused:
            pause_screen(
                screen,
                save_message_timer,
                pause_bild
            )
            if save_message_timer > 0:
                save_message_timer -= 1
            clock.tick(60)
            continue
        screen.fill("black")
        table_rect, stairs_rect = Attic(screen)
        obstacles = [table_rect, stairs_rect] + walls
        player.move(obstacles)
        player.interact(screen=screen)
        if diary_open == True:
            diary.draw()
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()