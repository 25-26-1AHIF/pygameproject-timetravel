import pygame
from assets.Game_Variables.game_variables import GameVariables as GV

pygame.init() 
pygame.display.set_caption("TimeTravel - Main")
screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    running = False
    pygame.display.flip()
pygame.quit() 