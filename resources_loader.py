import pygame
from config import resourcesPath


def getRes(res: str) -> pygame.surface.Surface:
    return pygame.image.load(resourcesPath[res]).convert_alpha()


# 资源加载
class ResourcesLoader:
    @staticmethod
    def loadAllResources():

        ResourcesLoader.message = getRes("message")
        ResourcesLoader.gameover = getRes("gameover")

        ResourcesLoader.background = {}
        ResourcesLoader.background["day"] = getRes("background-day")
        ResourcesLoader.background["night"] = getRes("background-night")
        ResourcesLoader.base = getRes("base")

        ResourcesLoader.bird = {}
        ResourcesLoader.bird["red"] = (getRes("redbird-downflap"), getRes("redbird-midflap"), getRes("redbird-upflap"))
        ResourcesLoader.bird["blue"] = (getRes("bluebird-downflap"), getRes("bluebird-midflap"), getRes("bluebird-upflap"))
        ResourcesLoader.bird["yellow"] = (getRes("yellowbird-downflap"), getRes("yellowbird-midflap"), getRes("yellowbird-upflap"))

        ResourcesLoader.pipe = {}
        ResourcesLoader.pipe["red"] = getRes("pipe-red")
        ResourcesLoader.pipe["green"] = getRes("pipe-green")

        ResourcesLoader.num = {}
        for i in range(10):
            ResourcesLoader.num[i] = getRes(str(i))
