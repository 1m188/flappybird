import random
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import QTimer
import config


# scene basic class
class Scene(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.prepare()

    def run(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.frame)
        self.timer.start(1000 / config.FPS)

    def stop(self):
        self.timer.stop()
        self.end()

    def frame(self):
        self.status()
        self.update()

    def prepare(self):
        pass

    def status(self):
        pass

    def end(self):
        pass


# 开始场景
class StartScene(Scene):
    def prepare(self):
        self.setFixedSize(config.screenWidth, config.screenHeight)
        index = random.randint(0, len(config.ImgRes.background) - 1)
        key = list(config.ImgRes.background.keys())[index]
        self.background = config.ImgRes.background[key]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.background)
        super().paintEvent(event)
