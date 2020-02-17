import pygame
from config import resourcesPath


def getRes(res: str) -> pygame.surface.Surface:
    return pygame.image.load(resourcesPath[res]).convert_alpha()


# 资源加载
class ResourcesLoader:
    @classmethod
    def loadAllResources(cls):

        cls.message = getRes("message")
        cls.gameover = getRes("gameover")

        cls.background = {}
        cls.background["day"] = getRes("background-day")
        cls.background["night"] = getRes("background-night")
        cls.base = getRes("base")

        cls.bird = {}
        cls.bird["red"] = (getRes("redbird-downflap"), getRes("redbird-midflap"), getRes("redbird-upflap"))
        cls.bird["blue"] = (getRes("bluebird-downflap"), getRes("bluebird-midflap"), getRes("bluebird-upflap"))
        cls.bird["yellow"] = (getRes("yellowbird-downflap"), getRes("yellowbird-midflap"), getRes("yellowbird-upflap"))

        cls.pipe = {}
        cls.pipe["red"] = getRes("pipe-red")
        cls.pipe["green"] = getRes("pipe-green")

        cls.num = {}
        for i in range(10):
            cls.num[i] = getRes(str(i))
