import pygame
from src.Game_Variables.game_variables import GameVariables as GV
from src.Game_Variables.game_variables import GameScreens

def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Main")
    GV.init()

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

    main_screen_bild = pygame.image.load("assets/Sprites/Main_Screen-Bild.png")
    screen.blit(source=main_screen_bild, dest=(0, 0))

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
