import pygame

def medieval_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Medieval-Screen")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        pygame.display.flip()
    pygame.quit()