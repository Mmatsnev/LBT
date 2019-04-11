#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from GenerateRandomNumbers import GenerateRandomNumbers, WriteToFile
from PyQt5 import QtWidgets, QtCore, QtGui

class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.PushButtonGenerateRandomNumbers = QtWidgets.QPushButton("生成随机数", self)
        self.PushButtonGenerateRandomNumbers.move(200, 40)
        self.PushButtonGenerateRandomNumbers.clicked.connect(self.GenerateRandomNumbersIRQ)

        self.LineEditGetNumber = QtWidgets.QLineEdit(self)
        self.LineEditGetNumber.move(20, 40)

        # 限制单行文本输入框输入
        self.pIntValidator = QtGui.QIntValidator(self)
        self.pIntValidator.setRange(1, 1000000)
        self.LineEditGetNumber.setValidator(self.pIntValidator)

        self.TextEditRandomData = QtWidgets.QTextEdit(self)
        self.TextEditRandomData.move(20, 80)

        self.resize(400, 600)
        self.setWindowTitle("生成随机数")
        self.move(20, 50)
        self.show()

    def GenerateRandomNumbersIRQ(self):
        if self.LineEditGetNumber.text():
            number = int(self.LineEditGetNumber.text())
        else:
            number = 256
        self.TextEditRandomData.setText(GenerateRandomNumbers(number))
        WriteToFile(GenerateRandomNumbers(number))
        print("ts")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
