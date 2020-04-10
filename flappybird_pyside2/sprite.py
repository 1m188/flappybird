import random
from PySide2.QtGui import QPixmap
import config


# sprite basic class
class Sprite:
    def __init__(self, image: QPixmap):
        self.spriteImg = image
        self.x = 0
        self.y = 0

    @property
    def width(self):
        return self.spriteImg.width()

    def height(self):
        return self.spriteImg.height()

    # 每一帧的变化
    def update(self):
        pass


# 小鸟
class Bird(Sprite):
    def __init__(self):
        index = random.randint(0, len(config.ImgRes.bird) - 1)
        key = list(config.ImgRes.bird.keys())[index]
        self.imageGroup = config.ImgRes.bird[key]
        super().__init__(self.imageGroup[0])
