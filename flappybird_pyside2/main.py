import sys
from PySide2.QtWidgets import QApplication
from window import Window
import config

app = QApplication(sys.argv)
config.ImgRes.loadAll()
config.AudRes.loadAll()
w = Window()
w.show()
app.exec_()
