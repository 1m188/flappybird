from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import QTimer
import config
from sprite import Bird, Background, Message


# 场景类
class Scene(QWidget):
    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(parent)
        self.resize(self.parentWidget().size())  # 使场景和窗口大小一样大
        self.prepare(*args, **kwargs)  # 场景开始前的准备

    # 场景启动，使用定时器控制帧数
    def run(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.frame)
        self.timer.start(1000 / config.FPS)

    # 场景停止，进入扫尾阶段
    def stop(self):
        self.timer.stop()
        self.end()

    # 每帧的内容
    def frame(self):
        self.statusUpdate()
        self.update()  # 刷新重绘

    def prepare(self, *args, **kwargs):
        pass

    # 场景每帧的某些状态的变化
    def statusUpdate(self):
        pass

    # 场景结束的扫尾
    def end(self):
        pass


# 开始场景
class StartScene(Scene):
    def prepare(self, background: Background, bird: Bird):
        self.background = background  # 背景

        # 鸟
        self.bird = bird
        self.bird.x = self.width() / 8
        self.bird.y = self.height() / 3 + 42

        # 开场信息
        self.message = Message()
        self.message.x = self.width() / 2 - self.message.width / 2
        self.message.y = self.height() / 12

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background.x, self.background.y, self.background.spriteImg)
        painter.drawPixmap(self.bird.x, self.bird.y, self.bird.spriteImg)
        painter.drawPixmap(self.message.x, self.message.y, self.message.spriteImg)
        super().paintEvent(event)

    def statusUpdate(self):
        self.background.moveLeft()  # 背景移动，制造前飞效果
        self.bird.changeImg()  # 鸟更换图片，制造翅膀效果

    # 一旦鼠标点击，立刻停止开始场景，进入下一个游戏场景
    def mousePressEvent(self, event):
        self.stop()
        super().mousePressEvent(event)

    # 扫尾，生成游戏场景并准备进入
    def end(self):
        self.deleteLater()
        gameScene = GameScene(self.parent(), self.background, self.bird)
        gameScene.show()
        gameScene.run()


# 游戏场景
class GameScene(Scene):
    def prepare(self, background: Background, bird: Bird):
        self.background = background
        self.bird = bird
        self.bird.initStatus()  # 初始化小鸟状态

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background.x, self.background.y, self.background.spriteImg)
        painter.drawPixmap(self.bird.x, self.bird.y, self.bird.spriteImg)
        super().paintEvent(event)

    # 点击鼠标让小鸟往上飞
    def mousePressEvent(self, event):
        self.bird.v = -config.birdRevSpd
        super().mousePressEvent(event)

    # 背景不断移动
    # 同时每帧的变化小鸟需要按照一定加速度向下走
    def statusUpdate(self):
        self.background.moveLeft()
        self.bird.changeImg()

        self.bird.v += config.gravity
        self.bird.y += self.bird.v
