import pygame
from resources_loader import ResourcesLoader
import config


class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image = ResourcesLoader.base
        self.rect = pygame.Rect(0, 0, image.get_width() * 2, image.get_height())
        self.rect.bottom = config.screenHeight
        self.image = pygame.surface.Surface(self.rect.size).convert()
        self.image.blit(image, pygame.Rect(0, 0, self.rect.width / 2, self.rect.height))
        self.image.blit(image, pygame.Rect(self.rect.width / 2, 0, self.rect.width / 2, self.rect.height))

    def update(self):
        self.rect.left -= config.baseScrollSpeed
        if self.rect.right <= config.screenWidth:
            self.rect.left = 0
