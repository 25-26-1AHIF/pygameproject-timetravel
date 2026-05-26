import pygame
from assets.Game_Variables.game_variables import GameVariables as GV
from assets.Game_Variables.game_variables import GameScreens
from src.assets.game.diary import diary
from src.assets.game.sprites import Sprite
from src.assets.game.Attic import Attic
from src.assets.Game_Variables.player_variables import Player


def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Main")

    titel_text = GV.FONT_BIG.render("TimeTravel", True, "white")
    untertext = GV.FONT_SMALL.render("Was für ein Geheimnis kann ein Tagebuch beherbergen?", True, "white")
    starten_text = GV.FONT_BUTTONS.render("Starten", True, "white")
    laden_text = GV.FONT_BUTTONS.render("Spielstand laden", True, "white")
    beenden_text = GV.FONT_BUTTONS.render("Beenden", True, "white")

    titel_text_rect = titel_text.get_rect(center=(GV.SCREEN_WIDTH/2, 100))
    untertext_rect = untertext.get_rect(center=(GV.SCREEN_WIDTH/2, 150))
    starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH/2, 350))
    laden_text_rect = laden_text.get_rect(center=(GV.SCREEN_WIDTH/2, 400))
    beenden_text_rect = beenden_text.get_rect(center=(GV.SCREEN_WIDTH/2, 450))

    main_screen_bild = pygame.image.load("assets/Bilder/Main_Screen-Bild.png")
    screen.blit(source=main_screen_bild, dest=(0,0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                elif laden_text_rect.collidepoint(event.pos):
                    return GameScreens.LADEN
                elif beenden_text_rect.collidepoint(event.pos):
                    running = False

        screen.blit(source=titel_text, dest=titel_text_rect)
        screen.blit(source=untertext, dest=untertext_rect)
        pygame.draw.rect(surface=screen, rect=starten_text_rect, color="dark green", width=0)
        pygame.draw.rect(surface=screen, rect=laden_text_rect, color="dark green", width=0)
        pygame.draw.rect(surface=screen, rect=beenden_text_rect, color="dark green", width=0)
        screen.blit(source=starten_text, dest=starten_text_rect)
        screen.blit(source=laden_text, dest=laden_text_rect)
        screen.blit(source=beenden_text, dest=beenden_text_rect)


        pygame.display.flip()
    pygame.quit()

def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Play-Screen")

    player = Player()

    walls = [
        pygame.Rect(90, 185, 900, 20),
        pygame.Rect(90, 670, 900, 20),
        pygame.Rect(90, 185, 20, 500),
        pygame.Rect(970, 185, 20, 500),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill("black")


        tabele_rect = Attic(screen)

        obstacles = [tabele_rect] + walls
        player.move(obstacles)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def main():
    GV.init()
    screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    while True:
        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen=screen, clock=clock)
        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen=screen, clock=clock)
    pygame.quit()

if __name__ == "__main__":
    main()