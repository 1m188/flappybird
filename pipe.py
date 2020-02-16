import random
import pygame
from resources_loader import ResourcesLoader
import config


def getPipe(baseHeight: int) -> tuple:
    pipeAbove = Pipe(True)
    pipeBelow = Pipe(False)
    pipeBelow.rect.top = random.randint(config.pipeLimit + config.pipeInterval, config.screenHeight - baseHeight - config.pipeLimit)
    pipeAbove.rect.bottom = pipeBelow.rect.top - config.pipeInterval
    return pipeAbove, pipeBelow


class Pipe(pygame.sprite.Sprite):
    def __init__(self, isAbove: bool):
        super().__init__()

        self.image = ResourcesLoader.pipe["green"]
        if isAbove:
            self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.left = config.screenWidth

    def update(self):
        self.rect.left -= config.pipeScrollSpeed
        if self.rect.right <= 0:
            self.kill()
