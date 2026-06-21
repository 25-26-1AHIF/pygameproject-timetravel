import pygame
from src.Game_Variables.game_variables import GameScreens
from src.game.player import Player
from src.Game_Variables.game_variables import GameVariables as GV
from src.game.pause_screen import pause_screen
from src.game.Attic import Attic
from src.Game_Variables.save_system import save_game
from src.Game_Variables.save_system import load_game
from src.game.diary import diary as diary_ausfuehren
from src.Game_Variables.game_variables import GameObject
from src.game.sprites import Tilemap

def play_screen(screen: pygame.Surface, clock: pygame.time.Clock, load_save=False):
    GV.init()
    diary_open = False
    pygame.display.set_caption("TimeTravel - Play-Screen")
    pause_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png").convert()
    pause_bild = pygame.transform.scale(pause_bild, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    player = Player()
    diary = diary_ausfuehren(screen=screen, filepath="assets/Sprites/Diary/Diary.png")
    medieval_icon_rect = diary.icon_klein.get_rect(topleft=diary.medievel_icon_pos)
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
    font = pygame.font.SysFont("Georgia", 32)
    image_ui_rect = pygame.Rect(0,0, 33, 33)
    tilemap_ui = Tilemap("assets/Sprites/UI_Pack/Tilesheets/Large tiles/Thin outline/tilemap.png", (13,7), image_ui_rect)
    tilemap_ui = tilemap_ui.load_spritesheet()

    image_ui_small_rect = pygame.Rect(0,0,17,17)
    tilemap_ui_small = Tilemap("assets/Sprites/UI_Pack/Tilesheets/Small tiles/Thin outline/tilemap.png", (23,7), image_ui_small_rect)
    tilemap_ui_small = tilemap_ui_small.load_spritesheet()

    banner_welcome_map = [
        [(4,4),(4,5),(4,6)]
    ]
    banner_welcome_obj = GameObject(tilemap_ui, banner_welcome_map,  GV.SCREEN_WIDTH/2 - 200, 220, 100, 400, 32, 32)

    button_map = [
        [(2,3)]
    ]
    button_obj = GameObject(tilemap_ui_small, button_map, GV.SCREEN_WIDTH/2 - 70, 460, 75, 130, 16, 16)
    button_rect = pygame.Rect(GV.SCREEN_WIDTH/2 - 70, 460, 130, 75)

    font_mini = pygame.font.SysFont("Georgia", 18)
    text_intro = font_mini.render("Welcome in the Attic of your Grandpa!", True, "black")
    text_intro2 = font_mini.render("You wanted to flee the noise of the family gathering downstairs", True, "black")
    text_intro3 = font_mini.render("so you climbed up here. On the table you finda mysterious diary", True, "black")
    text_intro4 = font_mini.render("and when you open it, you click on the foto in there.", True, "black")
    text_intro5 = font_mini.render("By doing so, you teleport to a medieval village and have to find", True, "black")
    text_intro6 = font_mini.render("3 objects. You are being timed, so be fast. Once you collected them,", True, "black")
    text_intro7 = font_mini.render("you can enter the portal there and come back here. Have fun!", True, "black")
    text_ok_button = font_mini.render("Okay", True, "black")
    welcome_text = font.render("Welcome", True, "black")

    ok_button = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if action and event.key == pygame.K_e:
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
                if medieval_icon_rect.collidepoint(event.pos) and diary_open:
                   return GameScreens.MEDIEVAL
                if button_rect.collidepoint(event.pos):
                    GV.INTRO_BUTTON = True
                    ok_button = True
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
        table_rect, stairs_rect, table_collision_rect = Attic(screen)
        interactables = [
            {"rect": table_rect, "action": "diary"},
        ]
        obstacles = [table_collision_rect, stairs_rect] + walls
        action = player.interact(interactables)
        player.move(obstacles)
        if action:
            font = pygame.font.SysFont("Georgia", 32)
            text = font.render("Press E to interact", True, (255, 255, 255))
            screen.blit(text, (player.x - 150,player.y - 40))
        if diary_open:
            diary.draw()
        player.draw(screen)
        if not GV.INTRO_BUTTON:
            if not ok_button:
                pygame.draw.rect(screen, "brown", (GV.SCREEN_WIDTH / 2 - 275, 300, 550, 200))
                screen.blit(text_intro, (GV.SCREEN_WIDTH / 2 - 160, 320))
                screen.blit(text_intro2, (GV.SCREEN_WIDTH / 2 - 250, 340))
                screen.blit(text_intro3, (GV.SCREEN_WIDTH / 2 - 250, 360))
                screen.blit(text_intro4, (GV.SCREEN_WIDTH / 2 - 250, 380))
                screen.blit(text_intro5, (GV.SCREEN_WIDTH / 2 - 250, 400))
                screen.blit(text_intro6, (GV.SCREEN_WIDTH / 2 - 250, 420))
                screen.blit(text_intro7, (GV.SCREEN_WIDTH / 2 - 250, 440))
                banner_welcome_obj.draw(screen)
                screen.blit(welcome_text, (GV.SCREEN_WIDTH/2 - 65, 250))
                button_obj.draw(screen)
                screen.blit(text_ok_button, (GV.SCREEN_WIDTH/2 - 30, 485))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()