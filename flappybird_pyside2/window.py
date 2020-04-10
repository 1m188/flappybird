from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
import config
from scene import StartScene


# game main window
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        startScene = StartScene(self)
        startScene.run()

    def initUI(self):
        self.setWindowTitle(self.tr("Flappy Bird"))
        self.setFixedSize(config.screenWidth, config.screenHeight)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(config.ImgRes.icon)
