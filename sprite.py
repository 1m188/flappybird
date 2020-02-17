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


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        kind = ("yellow", "red", "blue")
        self.imgTpl = list(ResourcesLoader.bird[random.sample(kind, 1)[0]])
        temp = self.imgTpl.copy()
        temp.reverse()
        temp.pop(0)
        temp.pop(-1)
        self.imgTpl += temp

        self.imgIndex = 0
        self.image = self.imgTpl[self.imgIndex]
        self.rect = self.image.get_rect()
        self.init()

        # 切换图像显示事件
        pygame.time.set_timer(pygame.USEREVENT + config.birdChangeImgEventID, config.birdImgChangeEventInterval)

    def init(self):
        self.speed = 0
        self.rect.top = config.screenHeight / 2 - 49
        self.rect.left = config.screenWidth / 10

    def update(self):
        self.speed += config.gravity
        self.rect.top += self.speed

    def speedReverse(self):
        self.speed = -config.birdRevSpd

    def changeImg(self):
        self.imgIndex += 1
        index = self.imgIndex % len(self.imgTpl)
        self.image = self.imgTpl[index]

    def isDead(self, baseTop, pipeGroup):
        if self.rect.bottom >= baseTop or self.rect.top <= 0:
            return True
        if pygame.sprite.spritecollide(self, pipeGroup, False):
            return True
        return False


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
