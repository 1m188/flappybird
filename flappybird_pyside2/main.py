import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QCoreApplication, Qt
import pygame

from window import Window
import config

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 添加高分屏支持
pygame.init()  # 初始化pygame

app = QApplication(sys.argv)

# 加载资源
config.ImgRes.loadAll()
config.AudRes.loadAll()

# 窗口显示
w = Window()
w.show()

app.exec_()
