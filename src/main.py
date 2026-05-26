import pygame

from assets.Game_Variables.game_variables import GameVariables as GV
from assets.Game_Variables.game_variables import GameScreens
from assets.Game_Variables.save_system import save_game, load_game

from src.assets.game.Attic import Attic
from src.assets.Game_Variables.player_variables import Player


def pause_screen(screen: pygame.Surface, save_message_timer, pause_bild):
    screen.blit(pause_bild, (0, 0))

    overlay = pygame.Surface((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    overlay.set_alpha(130)
    overlay.fill((0, 0, 0))

    pause_text = GV.FONT_BIG.render("PAUSIERT", True, "white")
    info_text = GV.FONT_SMALL.render(
        "ESC = weiter | S = speichern | M = Menü | Q = Beenden",
        True,
        "white"
    )

    screen.blit(overlay, (0, 0))
    screen.blit(pause_text, pause_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 - 40)))
    screen.blit(info_text, info_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 + 30)))

    if save_message_timer > 0:
        save_text = GV.FONT_SMALL.render("Erfolgreich gespeichert!", True, "light green")
        screen.blit(save_text, save_text.get_rect(center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 + 90)))

    pygame.display.flip()


def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Main")

    titel_text = GV.FONT_BIG.render("TimeTravel", True, "white")
    untertext = GV.FONT_SMALL.render("Was für ein Geheimnis kann ein Tagebuch beherbergen?", True, "white")
    starten_text = GV.FONT_BUTTONS.render("Starten", True, "white")
    laden_text = GV.FONT_BUTTONS.render("Spielstand laden", True, "white")
    beenden_text = GV.FONT_BUTTONS.render("Beenden", True, "white")

    titel_text_rect = titel_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 100))
    untertext_rect = untertext.get_rect(center=(GV.SCREEN_WIDTH / 2, 150))
    starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 350))
    laden_text_rect = laden_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 400))
    beenden_text_rect = beenden_text.get_rect(center=(GV.SCREEN_WIDTH / 2, 450))

    main_screen_bild = pygame.image.load("assets/Bilder/Main_Screen-Bild.png").convert()
    main_screen_bild = pygame.transform.scale(main_screen_bild, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                elif laden_text_rect.collidepoint(event.pos):
                    return GameScreens.LADEN
                elif beenden_text_rect.collidepoint(event.pos):
                    return None

        screen.blit(main_screen_bild, (0, 0))

        screen.blit(titel_text, titel_text_rect)
        screen.blit(untertext, untertext_rect)

        pygame.draw.rect(screen, "dark green", starten_text_rect)
        pygame.draw.rect(screen, "dark green", laden_text_rect)
        pygame.draw.rect(screen, "dark green", beenden_text_rect)

        screen.blit(starten_text, starten_text_rect)
        screen.blit(laden_text, laden_text_rect)
        screen.blit(beenden_text, beenden_text_rect)

        pygame.display.flip()
        clock.tick(60)


def play_screen(screen: pygame.Surface, clock: pygame.time.Clock, load_save=False):
    pygame.display.set_caption("TimeTravel - Play-Screen")

    pause_bild = pygame.image.load("assets/Bilder/Main_Screen-Bild.png").convert()
    pause_bild = pygame.transform.scale(pause_bild, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

    player = Player()

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
            pause_screen(screen, save_message_timer, pause_bild)

            if save_message_timer > 0:
                save_message_timer -= 1

            clock.tick(60)
            continue

        screen.fill("black")

        table_rect, stairs_rect = Attic(screen)
        obstacles = [table_rect, stairs_rect] + walls

        player.move(obstacles)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)


def main():
    GV.init()

    screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    GameScreens.actual = GameScreens.MAIN

    while GameScreens.actual is not None:
        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen, clock)

        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen, clock, load_save=False)

        elif GameScreens.actual == GameScreens.LADEN:
            GameScreens.actual = play_screen(screen, clock, load_save=True)

    pygame.quit()


if __name__ == "__main__":
    main()