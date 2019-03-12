#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore

class test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button1 = QtWidgets.QPushButton("显示", self)
        
        self.button1.clicked.connect(self.showwidget)
        self.HBoxLayout1 = QtWidgets.QGridLayout()

        self.WidgetShow = QtWidgets.QWidget(self)
        self.WidgetShow.resize(300, 300)
        self.WidgetShow.move(20, 20)
        # self.WidgetShow.setGeometry(QtCore.QRect(100, 100, 100, 100))
        self.HBoxLayout = QtWidgets.QHBoxLayout(self.WidgetShow)
        self.HBoxLayout.addLayout(self.HBoxLayout1)
        # self.HBoxLayout.setContentsMargins(50, 50, 200, 200)
        
        

        self.HBoxLayout1.addWidget(self.button1, 0, 0)
        # self.button1.move(50, 50)
        self.setWindowTitle("test")
        self.resize(500, 400)
        self.move(50, 20)
        self.show()

    def showwidget(self):
        print("dianjil")
        # self.button2 = QtWidgets.QPushButton("show", self)
        # self.HBoxLayout1.addWidget(self.button2)

        self.tableWidgetShowIOStruct = QtWidgets.QTableWidget(self)
        self.tableWidgetShowIOStruct.setRowCount(4)
        self.tableWidgetShowIOStruct.setColumnCount(3)
        self.HBoxLayout1.addWidget(self.tableWidgetShowIOStruct, 0, 1, 4, 4)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    te = test()
    sys.exit(app.exec_())