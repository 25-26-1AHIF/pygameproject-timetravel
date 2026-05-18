import pygame
from assets.Game_Variables.game_variables import GameVariables as GV
from assets.Game_Variables.game_variables import GameScreens
def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Main")

    titel_text = GV.FONT_BIG.render("TimeTravel", True, "white")
    untertext = GV.FONT_SMALL.render("Was für ein Geheimnis kann ein Tagebuch beherbergen?", True, "white")
    starten_text = GV.FONT_BUTTONS.render("Starten", True, "white")
    laden_text = GV.FONT_BUTTONS.render("Spielstand laden", True, "white")
    beenden_text = GV.FONT_BUTTONS.render("Beenden", True, "white")

    titel_text_rect = titel_text.get_rect(center=(GV.SCREEN_WIDTH/2, 100))
    untertext_rect = untertext.get_rect(center=(GV.SCREEN_WIDTH/2, 150))
    starten_text_rect = starten_text.get_rect(center=(GV.SCREEN_WIDTH/2, 250))
    laden_text_rect = laden_text.get_rect(center=(GV.SCREEN_WIDTH/2, 300))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        running = False
        pygame.display.flip()
    pygame.quit()

def main():
    GV.init()
    screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    while True:
        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen=screen, clock=clock)
    pygame.quit()

if __name__ == "__main__":
    main()