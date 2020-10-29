import config

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from scene import StartScene
from sprite import Background, Bird, Base


# 游戏窗口
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # 开始场景启动
        startScene = StartScene(self, Background(), Bird(), Base())
        startScene.run()

    def initUI(self):
        self.setWindowTitle(self.tr("Flappy Bird"))
        self.setFixedSize(config.screenWidth, config.screenHeight)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(config.ImgRes.icon)
