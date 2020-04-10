from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import QTimer
import config
from sprite import Bird, Background


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
        self.background = Background()
        self.bird = Bird()
        self.bird.x = self.width() / 8
        self.bird.y = self.height() / 3

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background.x, self.background.y, self.background.spriteImg)
        painter.drawPixmap(self.bird.x, self.bird.y, self.bird.spriteImg)
        super().paintEvent(event)

    def status(self):
        self.background.update()
