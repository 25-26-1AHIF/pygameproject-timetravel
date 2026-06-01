import pygame
from src.Game_Variables.game_variables import GameVariables as GV
class Player:

    def __init__(self):
        self.x = 200
        self.y = 400
        self.speed = 15
        self.direction = "down"

        sheet = pygame.image.load("assets/Sprites/Characters/Male person/Player.TopDown.png").convert_alpha()

        sheet = pygame.transform.scale(sheet, (512, 512))

        self.down = sheet.subsurface((56, 40, 67, 122))
        self.left = sheet.subsurface((56, 190, 67, 122))
        self.up = sheet.subsurface((56, 340, 67, 122))
        self.right = pygame.transform.flip(self.left, True, False)

        self.image = self.down


    def move(self, obstacles):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "left"
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "right"
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "up"
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "down"

        if self.direction == "left":
            self.image = self.left
        elif self.direction == "right":
            self.image = self.right
        elif self.direction == "up":
            self.image = self.up
        elif self.direction == "down":
            self.image = self.down

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 67, 122)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y, 67, 122))
        pygame.draw.rect(screen, pygame.Color("black"), (self.x, self.y, 67, 122), width=1)

    def interact(self, screen) -> bool:
        if self.x > 700 and self.x < 880 and self.y > 350 and self.y < 500:
            interact_font = pygame.font.SysFont("Georgia", 32, False, False)
            interact_text = interact_font.render("Press 'E' to interact", True, (245, 230, 200))
            interact_text_rect = interact_text.get_rect(center=(GV.SCREEN_WIDTH/2, GV.SCREEN_HEIGHT/2))
            screen.blit(interact_text, interact_text_rect)
            return True
        else:
            return False