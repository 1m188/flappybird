from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter
import config


# game main window
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.tr("Flappy Bird"))
        self.setFixedSize(288, 512)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(config.ImgRes.icon)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, config.ImgRes.background["day"])
        super().paintEvent(event)
