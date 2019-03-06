#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore

class TestRadio(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.initRadioButton()
        # self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle("Test Radio")
        self.show()

    def initRadioButton(self):
        self.gridLayoutModuleSelect = QtWidgets.QGridLayout(self)
        self.radioGroup = QtWidgets.QButtonGroup(self)

        self.radioButtonADC = QtWidgets.QRadioButton("ADC", self)
        self.radioGroup.addButton(self.radioButtonADC)
        self.gridLayoutModuleSelect.addWidget(self.radioButtonADC, 0, 0)

        self.radioButtonSCI = QtWidgets.QRadioButton("SCI", self)
        self.radioGroup.addButton(self.radioButtonSCI)
        self.gridLayoutModuleSelect.addWidget(self.radioButtonSCI, 0, 2)

        self.radioButtonUART = QtWidgets.QRadioButton("UART", self)
        self.radioGroup.addButton(self.radioButtonUART)
        self.gridLayoutModuleSelect.addWidget(self.radioButtonUART, 1, 0)

        self.radioButtonSPI = QtWidgets.QRadioButton("SPI", self)
        self.radioGroup.addButton(self.radioButtonSPI)
        self.gridLayoutModuleSelect.addWidget(self.radioButtonSPI, 1, 1)

        self.radioGroup.buttonClicked.connect(self.radioButtonFuc)

        self.gridLayoutModuleSelect.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutModuleSelect.setHorizontalSpacing(10)
        self.gridLayoutModuleSelect.setVerticalSpacing(10)
        
    
    def radioButtonFuc(self):
        print(self.radioGroup.checkedButton().text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = TestRadio()
    sys.exit(app.exec_())