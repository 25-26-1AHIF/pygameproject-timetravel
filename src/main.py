import pygame
from Game_Variables.game_variables import GameVariables as GV
from Game_Variables.game_variables import GameScreens
from game.play_screen import play_screen
from game.main_screen import main_screen
from game.medieval_screen import medieval_screen

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
        elif GameScreens.actual == GameScreens.MEDIEVAL:
            GameScreens.actual = medieval_screen(screen, clock)
    pygame.quit()

if __name__ == "__main__":
    main()