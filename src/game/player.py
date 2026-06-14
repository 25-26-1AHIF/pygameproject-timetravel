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

        dx = 0
        dy = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -self.speed
            self.direction = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed
            self.direction = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -self.speed
            self.direction = "up"
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.speed
            self.direction = "down"

        new_rect = self.get_rect().move(dx, dy)

        collision = False
        for obstacle in obstacles:
            if new_rect.colliderect(obstacle):
                collision = True
                break

        if not collision:
            self.x += dx
            self.y += dy

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
       # pygame.draw.rect(screen, pygame.Color("black"), (self.x, self.y, 67, 122), width=1)

    def interact(self, interactables: list):
        for obj in interactables:
            if self.get_rect().colliderect(obj["rect"]):
                return obj["action"]
        return None
