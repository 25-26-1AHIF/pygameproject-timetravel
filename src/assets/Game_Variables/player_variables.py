import pygame

class Player:

    def __init__(self):
        self.x = 200
        self.y = 400
        self.speed = 15
        self.direction = "down"

        sheet = pygame.image.load(
            "assets/Sprites/Characters/Male person/Player.TopDown.png"
        ).convert_alpha()

        sheet = pygame.transform.scale(sheet, (512, 512))

        self.down = sheet.subsurface((56, 40, 67, 122))
        self.left = sheet.subsurface((56, 190, 67, 122))
        self.up = sheet.subsurface((56, 340, 67, 122))
        self.right = pygame.transform.flip(self.left, True, False)

        self.image = self.down
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, obstacles):
        keys = pygame.key.get_pressed()

        old_x = self.x
        old_y = self.y

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

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                self.x = old_x
                self.y = old_y
                self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)