import random
from PySide2.QtGui import QPixmap, QPainter
from PySide2.QtCore import QTimer
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


# 标题信息
class Message(Sprite):
    def __init__(self):
        super().__init__(config.ImgRes.message)


# 小鸟
class Bird(Sprite):
    def __init__(self):
        index = random.randint(0, len(config.ImgRes.bird) - 1)
        key = list(config.ImgRes.bird.keys())[index]
        self.imgGroup = list(config.ImgRes.bird[key])
        another = self.imgGroup.copy()
        another.reverse()
        another.pop(0)
        another.pop()
        self.imgGroup = tuple(self.imgGroup + another)
        self.imgID = 0
        self.imgLen = len(self.imgGroup)
        super().__init__(self.imgGroup[self.imgID])
        self.imgID += 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.changeImg)
        self.timer.start(config.birdImgChangeEventInterval)

    def changeImg(self):
        if self.imgID >= self.imgLen:
            self.imgID = 0
        self.spriteImg = self.imgGroup[self.imgID]
        self.imgID += 1
