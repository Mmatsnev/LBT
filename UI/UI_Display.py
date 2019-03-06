#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import os
import json
sys.path.append('.')
from ChipModel_MH190x import ChipMH190x
from PyQt5.QtWidgets import (QMainWindow, QPushButton, 
    QApplication, QLineEdit)



class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.ButtonRefresh = QPushButton("刷新", self)
        self.ButtonRefresh.move(20, 20)
        self.ButtonRefresh.clicked.connect(self.Refresh)
        self.LineUart = QLineEdit(self)
        self.LineUart.move(20, 50)

        self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle("LBT")

    def Refresh(self):
        mh1902 = ChipMH190x("MH1902")

        self.LineUart.setText(mh1902.GetMH190xDataFromFile("MH1902")["UART"]["uart0"]["Rx0"]["Group"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())