from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt


# game main window
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.tr("Flappy Bird"))
        self.setFixedSize(288, 512)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
