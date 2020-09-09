import random
from PySide2.QtGui import QPixmap, QPainter
import config
from PySide2.QtCore import Signal, QObject


# 精灵类
class Sprite:
    def __init__(self, image: QPixmap):
        self.spriteImg = image
        # 精灵坐标
        self.x = 0
        self.y = 0

    # 宽
    @property
    def width(self):
        return self.spriteImg.width()

    # 高
    @property
    def height(self):
        return self.spriteImg.height()


# 背景
class Background(Sprite):
    def __init__(self):
        # 随机选择一个背景
        index = random.randint(0, len(config.ImgRes.background) - 1)
        key = list(config.ImgRes.background.keys())[index]
        background = config.ImgRes.background[key]

        # 做一个两倍宽的背景图片，便于制造移动飞行的效果
        image = QPixmap(background.width() * 2, background.height())
        painter = QPainter(image)
        painter.drawPixmap(0, 0, background)
        painter.drawPixmap(background.width(), 0, background)
        super().__init__(image)

    # 每帧左移，制造出小鸟不断往前飞的感觉
    def moveLeft(self):
        self.x -= config.backgroundScrollSpeed
        if self.x <= -self.width / 2:
            self.x = 0


# 标题信息
class Message(Sprite):
    def __init__(self):
        super().__init__(config.ImgRes.message)


# 小鸟
class Bird(Sprite, QObject):
    passPipe = Signal()

    def __init__(self):
        # 随机选择小鸟系列图片
        index = random.randint(0, len(config.ImgRes.bird) - 1)
        key = list(config.ImgRes.bird.keys())[index]
        self.imgGroup = list(config.ImgRes.bird[key])

        # 做小鸟的一系列动作图片列表
        another = self.imgGroup.copy()
        another.reverse()
        another.pop(0)
        another.pop()
        self.imgGroup = tuple(self.imgGroup + another)

        # 切换图片，制造小鸟扇动翅膀的效果
        self.imgID = 0
        self.imgLen = len(self.imgGroup)
        Sprite.__init__(self, self.imgGroup[self.imgID])
        self.imgID += 1
        self.frameCounter = 0

        QObject.__init__(self)

    # 初始化鸟的状态，速度等
    def initStatus(self):
        self.v = 0

    # 改变小鸟图片，制造出扇动翅膀的动画
    def changeImg(self):
        self.frameCounter += 1
        if self.frameCounter == config.birdImgChangeFrameNum:
            self.frameCounter = 0
            if self.imgID >= self.imgLen:
                self.imgID = 0
            self.spriteImg = self.imgGroup[self.imgID]
            self.imgID += 1
