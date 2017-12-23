#coding:euc-kr

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog,
                        QApplication)

app = QApplication([])
dialog = QInputDialog()
dialog.show()
app.exec_() # 얘에 의해서 실행된다.