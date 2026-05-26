import pygame

class Player:
    def __init__(self):
        self.x = 200
        self.y = 300
        self.speed = 10

        self.image = pygame.image.load(
            "assets/Sprites/Characters/Male person/Player.TopDown.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, (512, 512))
        self.image = self.image.subsurface((56, 40, 67, 122))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))