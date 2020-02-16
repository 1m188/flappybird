import random
import pygame
import config
from resources_loader import ResourcesLoader


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
