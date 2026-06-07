import pygame

class Sprite:
    def __init__(self, filepath: str, image_count: int, image_rect: pygame.Rect, animation_speed: int):
        self.filepath = filepath
        self.image_count = image_count
        self.image_rect = image_rect
        self.images: list[pygame.Surface] = []
        self.animation_speed = animation_speed

    def load_spritesheet(self) -> None:
        sprite_sheet = pygame.image.load(self.filepath).convert()

        for image_index in range(self.image_count):
            image_surface = pygame.Surface(self.image_rect.size).convert()
            image_surface.fill((0, 0, 0, 0))
            image_surface.blit(sprite_sheet, dest=(0,0),
                               area=pygame.Rect(image_index*self.image_rect.width,
                               self.image_rect.y,
                               self.image_rect.width,
                               self.image_rect.height))
            self.images.append(image_surface)

    def draw(self, screen: pygame.Surface, xpos: float | int, ypos: float | int, frame_counter: int):
        screen.blit(self.images[(frame_counter// self.animation_speed) % self.image_count], dest=(xpos, ypos))

class Tilemap:
    def __init__(self, filepath: str, image_count: tuple[int, int], image_rect: pygame.Rect):
        self.filepath = filepath
        self.image_count = image_count
        self.image_rect = image_rect
        self.images: list[list[pygame.Surface]] = []

    def load_spritesheet(self):
        sprite_sheet = pygame.image.load(self.filepath).convert_alpha()
        for image_index_y in range(self.image_count[1]):
            self.images.append([])
            for image_index_x in range(self.image_count[0]):
                image_surface = pygame.Surface(self.image_rect.size).convert_alpha()
                image_surface.blit(sprite_sheet, dest=(0,0),
                                   area=pygame.Rect(image_index_x*self.image_rect.width,
                                   image_index_y * self.image_rect.height,
                                   self.image_rect.width,
                                   self.image_rect.height))
                self.images[image_index_y].append(image_surface)
        return self.images

    # def draw(self, screen: pygame.Surface, xpos: float | int, ypos: float | int, frame_counter: int):
    #    screen.blit(self.images[(frame_counter// self.animation_speed) % self.image_count], dest=(xpos, ypos))