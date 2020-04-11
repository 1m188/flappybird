from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import QTimer
import config
from sprite import Bird, Background, Message


# scene basic class
class Scene(QWidget):
    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(parent)
        self.resize(self.parentWidget().size())
        self.prepare(*args, **kwargs)

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

    def prepare(self, *args, **kwargs):
        pass

    def status(self):
        pass

    def end(self):
        pass


# 开始场景
class StartScene(Scene):
    def prepare(self, background: Background, bird: Bird):
        self.background = background

        self.message = Message()
        self.message.x = self.width() / 2 - self.message.width / 2
        self.message.y = self.height() / 12

        self.bird = bird
        self.bird.x = self.width() / 8
        self.bird.y = self.height() / 3 + 42
        self.bird.timer.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.background.x, self.background.y, self.background.spriteImg)
        painter.drawPixmap(self.bird.x, self.bird.y, self.bird.spriteImg)
        painter.drawPixmap(self.message.x, self.message.y, self.message.spriteImg)
        super().paintEvent(event)

    def status(self):
        self.background.update()

    def mouseReleaseEvent(self, event):
        self.stop()
        super().mouseReleaseEvent(event)

    def end(self):
        pass


# 游戏场景
class GameScene(Scene):
    def prepare(self):
        pass
