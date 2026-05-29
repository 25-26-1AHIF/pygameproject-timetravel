import pygame
from src.game.diary import diary
from src.Game_Variables.game_variables import GameScreens
from src.Game_Variables.game_variables import Icons

def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("TimeTravel - Play-Screen")
    icon_medieval = Icons.icon_klein
    icon_medieval_rect = icon_medieval.get_rect()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if icon_medieval_rect.collidepoint(event.pos):
                    return GameScreens.MEDIEVAL
        screen.fill("black")
        diary_bild = diary(screen, "assets/Sprites/Diary/Diary.png")
        diary_bild.draw()

        pygame.display.flip()
    pygame.quit()
