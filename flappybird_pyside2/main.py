import sys
from PySide2.QtWidgets import QApplication
from window import Window
import config

from PySide2.QtCore import QCoreApplication, Qt

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 添加高分屏支持

app = QApplication(sys.argv)

# 加载资源
config.ImgRes.loadAll()
config.AudRes.loadAll()

# 窗口显示
w = Window()
w.show()

app.exec_()
