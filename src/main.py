import pygame
from Game_Variables.game_variables import GameVariables as GV
from Game_Variables.game_variables import GameScreens
from game.sprites import Tilemap
from src.game.main_screen import main_screen

def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Play-Screen")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill("black")

        pygame.display.flip()
    pygame.quit()

def main():
    GV.init()
    screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    tilemap = Tilemap("assets/Sprites/Town (medieval)/Tilemap/tilemap_packed.png", image_count=(12, 11),
                      image_rect=pygame.Rect(0, 0, 16, 16), animation_speed=0)
    tilemap.load_spritesheet()

    while True:
        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen=screen, clock=clock)
        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen=screen, clock=clock)
    pygame.quit()

if __name__ == "__main__":
    main()