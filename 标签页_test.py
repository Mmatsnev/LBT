#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class mainUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.TabWidget = QtWidgets.QTabWidget()

        self.Page1Widget = QtWidgets.QWidget()

        self.Page1GridLayout = QtWidgets.QGridLayout(self)
        self.Page1Widget.setLayout(self.Page1GridLayout)
        self.TabWidget.addTab(self.Page1Widget, "page1")
        
        self.Page2Widget = QtWidgets.QWidget()
        self.page2GridLayout = QtWidgets.QGridLayout(self)
        self.Page2Widget.setLayout(self.page2GridLayout)
        self.TabWidget.addTab(self.Page2Widget, "page2")

        self.TopLayout = QtWidgets.QVBoxLayout(self)
        self.TopLayout.addWidget(self.TabWidget)


        self.resize(400, 600)
        self.setWindowTitle("mainUI")
        self.move(20, 50)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = mainUI()
    sys.exit(app.exec_())