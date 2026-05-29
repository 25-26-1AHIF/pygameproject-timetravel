import pygame

from Game_Variables.game_variables import GameVariables as GV
from Game_Variables.game_variables import GameScreens
from Game_Variables.save_system import save_game, load_game

from game.Attic import Attic
from Game_Variables.player_variables import Player


def pause_screen(screen: pygame.Surface, save_message_timer, pause_bild):

    screen.blit(pause_bild, (0, 0))

    overlay = pygame.Surface((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    overlay.set_alpha(140)
    overlay.fill((0, 0, 0))

    pause_text = GV.FONT_BIG.render(
        "PAUSIERT",
        True,
        (245, 230, 200)
    )

    info_text = GV.FONT_SMALL.render(
        "ESC = weiter | S = speichern | M = Menü | Q = Beenden",
        True,
        (230, 210, 180)
    )

    screen.blit(overlay, (0, 0))

    screen.blit(
        pause_text,
        pause_text.get_rect(
            center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 - 40)
        )
    )

    screen.blit(
        info_text,
        info_text.get_rect(
            center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 + 30)
        )
    )

    if save_message_timer > 0:

        save_text = GV.FONT_SMALL.render(
            "Erfolgreich gespeichert!",
            True,
            "light green"
        )

        screen.blit(
            save_text,
            save_text.get_rect(
                center=(GV.SCREEN_WIDTH / 2, GV.SCREEN_HEIGHT / 2 + 90)
            )
        )

    pygame.display.flip()


def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):

    pygame.display.set_caption("TimeTravel - Main")

    title_font = pygame.font.SysFont(
        "Georgia",
        82,
        bold=True
    )

    subtitle_font = pygame.font.SysFont(
        "Georgia",
        28
    )

    button_font = pygame.font.SysFont(
        "Georgia",
        38
    )

    title_text = title_font.render(
        "TimeTravel",
        True,
        (245, 230, 200)
    )

    subtitle_text = subtitle_font.render(
        "Was für ein Geheimnis kann ein Tagebuch beherbergen?",
        True,
        (235, 220, 190)
    )

    new_game_text = button_font.render(
        "Neues Spiel",
        True,
        (255, 240, 210)
    )

    load_text = button_font.render(
        "Spielstand laden",
        True,
        (255, 240, 210)
    )

    quit_text = button_font.render(
        "Beenden",
        True,
        (255, 240, 210)
    )

    title_rect = title_text.get_rect(
        center=(GV.SCREEN_WIDTH / 2, 120)
    )

    subtitle_rect = subtitle_text.get_rect(
        center=(GV.SCREEN_WIDTH / 2, 180)
    )

    new_game_rect = new_game_text.get_rect(
        center=(GV.SCREEN_WIDTH / 2, 380)
    )

    load_rect = load_text.get_rect(
        center=(GV.SCREEN_WIDTH / 2, 445)
    )

    quit_rect = quit_text.get_rect(
        center=(GV.SCREEN_WIDTH / 2, 510)
    )

    Main_screen_bild = pygame.image.load(
        "assets/Sprites/Main_Screen-Bild.png"
    ).convert()

    Main_screen_bild = pygame.transform.scale(
        Main_screen_bild,
        (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT)
    )

    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return None

            if event.type == pygame.MOUSEBUTTONDOWN:

                if new_game_rect.collidepoint(event.pos):
                    return GameScreens.PLAY

                elif load_rect.collidepoint(event.pos):
                    return GameScreens.LADEN

                elif quit_rect.collidepoint(event.pos):
                    return None

        screen.blit(Main_screen_bild, (0, 0))

        shadow_title = title_font.render(
            "TimeTravel",
            True,
            (40, 20, 10)
        )

        screen.blit(
            shadow_title,
            title_rect.move(4, 4)
        )

        screen.blit(title_text, title_rect)
        screen.blit(subtitle_text, subtitle_rect)

        buttons = [
            ("Neues Spiel", new_game_rect),
            ("Spielstand laden", load_rect),
            ("Beenden", quit_rect),
        ]

        for text, rect in buttons:

            hover = rect.collidepoint(mouse_pos)

            color = (
                (255, 240, 210)
                if hover else
                (220, 195, 160)
            )

            label = button_font.render(
                text,
                True,
                color
            )

            label_rect = label.get_rect(
                center=rect.center
            )

            screen.blit(label, label_rect)

            if hover:

                pygame.draw.line(
                    screen,
                    color,
                    (label_rect.left, label_rect.bottom + 5),
                    (label_rect.right, label_rect.bottom + 5),
                    2
                )

        pygame.display.flip()
        clock.tick(60)


def play_screen(
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        load_save=False
):

    pygame.display.set_caption("TimeTravel - Play-Screen")

    pause_bild = pygame.image.load(
        "assets/Sprites/Main_Screen-Bild.png"
    ).convert()

    pause_bild = pygame.transform.scale(
        pause_bild,
        (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT)
    )

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