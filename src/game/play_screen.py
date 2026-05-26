import pygame
from src.game.diary import diary

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
        diary_bild = diary(screen, "assets/Sprites/Diary/Diary.png")
        diary_bild.draw()

        pygame.display.flip()
    pygame.quit()
