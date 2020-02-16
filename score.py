import pygame
from resources_loader import ResourcesLoader
import config


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.numDict = ResourcesLoader.num
        self.numWidth, self.numHeight = self.numDict[0].get_size()
        self.rect = pygame.Rect(0, config.screenHeight / 8 - self.numHeight / 2, config.screenWidth, self.numHeight)
        self.image = pygame.surface.Surface(self.rect.size).convert_alpha()
        self.score = 0

    def update(self):
        self.image.fill((0, 0, 0, 0))
        score = str(self.score)
        length = len(score)
        scoreWidth = length * self.numWidth
        startX = config.screenWidth / 2 - scoreWidth / 2
        for i in score:
            self.image.blit(self.numDict[int(i)], pygame.Rect(startX, 0, self.numWidth, self.numHeight))
            startX += self.numWidth
