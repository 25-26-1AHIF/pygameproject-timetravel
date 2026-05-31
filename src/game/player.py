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