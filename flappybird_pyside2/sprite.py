import random
from PySide2.QtGui import QPixmap, QPainter
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


# 背景
class Background(Sprite):
    def __init__(self):
        index = random.randint(0, len(config.ImgRes.background) - 1)
        key = list(config.ImgRes.background.keys())[index]
        background = config.ImgRes.background[key]
        image = QPixmap(background.width() * 2, background.height())
        painter = QPainter(image)
        painter.drawPixmap(0, 0, background)
        painter.drawPixmap(background.width(), 0, background)
        super().__init__(image)

    # 每帧左移，制造出小鸟不断往前飞的感觉
    def update(self):
        self.x -= config.backgroundScrollSpeed
        if self.x <= -self.width / 2:
            self.x = 0


# 小鸟
class Bird(Sprite):
    def __init__(self):
        index = random.randint(0, len(config.ImgRes.bird) - 1)
        key = list(config.ImgRes.bird.keys())[index]
        self.imageGroup = config.ImgRes.bird[key]
        super().__init__(self.imageGroup[0])
