import sys

from PyQt5.QtWidgets import *

app = QApplication(sys.env)

label = QLabel("Hello PyQt")

label.show()

app.exec_()