#coding:euc-kr

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog,
                        QApplication)

app = QApplication([])
dialog = QInputDialog()
dialog.show()
app.exec_() # �꿡 ���ؼ� ����ȴ�.