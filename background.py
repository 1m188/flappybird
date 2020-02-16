import random
import pygame
import config
from resources_loader import ResourcesLoader


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        kind = ("day", "night")
        image = ResourcesLoader.background[random.sample(kind, 1)[0]]
        self.rect = pygame.Rect(0, 0, config.screenWidth * 2, config.screenHeight)
        self.image = pygame.surface.Surface(self.rect.size).convert()
        self.image.blit(image, pygame.Rect(0, 0, self.rect.width / 2, self.rect.height))
        self.image.blit(image, pygame.Rect(self.rect.width / 2, 0, self.rect.width / 2, self.rect.height))

    def update(self):
        self.rect.left -= config.backgroundScrollSpeed
        if self.rect.right <= config.screenWidth:
            self.rect.left = 0
