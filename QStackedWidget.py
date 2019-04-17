#!usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class StackedWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
            self.resize(400, 600)
            self.setWindowTitle("Stacked")

            self.leftlist = QtWidgets.QListWidget()
            self.leftlist.insertItem(0, '联系方式')
            self.leftlist.insertItem(1, '个人信息')
            self.leftlist.insertItem(2, '教育程度')

