import sys
from PySide2.QtWidgets import QApplication
from window import Window

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()
