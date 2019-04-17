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

        self.stack1 = QtWidgets.QWidget()
        self.stack2 = QtWidgets.QWidget()
        self.stack3 = QtWidgets.QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QtWidgets.QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.addWidget(self.leftlist)
        self.hbox.addWidget(self.Stack)
        self.setLayout(self.hbox)
        self.leftlist.currentRowChanged.connect(self.display)

    def stack1UI(self):
        self.layout = QtWidgets.QFormLayout()
        self.layout.addRow("name", QtWidgets.QLineEdit())
        self.layout.addRow("addr", QtWidgets.QLineEdit())
        self.stack1.setLayout(self.layout)

    def stack2UI(self):
        self.layout = QtWidgets.QFormLayout()
        self.sex = QtWidgets.QHBoxLayout()
        self.sex.addWidget(QtWidgets.QRadioButton("man"))
        self.sex.addWidget(QtWidgets.QRadioButton("woman"))
        self.layout.addRow(QtWidgets.QLabel("gender"), self.sex)
        self.layout.addRow("Birthday", QtWidgets.QLineEdit())
        self.stack2.setLayout(self.layout)

    def stack3UI(self):
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(QtWidgets.QLabel("科目"))
        self.layout.addWidget(QtWidgets.QCheckBox("物理"))
        self.layout.addWidget(QtWidgets.QCheckBox("高数"))
        self.stack3.setLayout(self.layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    demo = StackedWidget()
    demo.show()
    sys.exit(app.exec_())
