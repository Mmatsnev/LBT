#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore

class TestRadio(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ChipModuleList = ["ADC", "UART", "SPI", "LCD", "DCMI", "PWM", "MIPI", "KeyBoard", "SCI", "I2C",
                "SDRAM", "SDIO", "ADC", "PSRAM"]
        self.initUI()
        

    def initUI(self):

        self.initRadioButton()
        self.resize(600, 400)
        self.move(50, 100)
        self.setWindowTitle("Test Radio")
        self.show()

    def initRadioButton(self):
        self.gridLayoutModuleSelect = QtWidgets.QGridLayout()
        # self.gridLayoutModuleSelect.SetMaximumSize(100, 100, 100, 100)
        self.gridLayoutModuleSelect.setObjectName("gridLayoutWidget")
        self.radioGroup = QtWidgets.QButtonGroup(self)

        # createVar = locals()
        # listTemp = range(len(self.ChipModuleList))
        # for i, s in enumerate(listTemp):
        #     createVar["radioButton" + i] = s
        names = self.__dict__
        print(names)
        for i in range(len(self.ChipModuleList)):
            names['radioButton' + self.ChipModuleList[i]] = QtWidgets.QRadioButton(self.ChipModuleList[i], self)
        # names.pop('ChipModuleList')
        # print(names)
        # for i in names:
        #     self.radioGroup.addButton(names[i])
        #     print(i)
        # self.radioGroup.addButton(self.radioButtonSDIO, self)
        # self.gridLayoutModuleSelect.addWidget(self.radioButtonSDIO, 3, 0)
        print(self.radioButtonSDIO)

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

        # self.gridLayoutModuleSelect.setContentsMargins(0, 0, 0, 0)
        # 设置grid 布局中相邻控件的间隔
        self.gridLayoutModuleSelect.setHorizontalSpacing(6)
        self.gridLayoutModuleSelect.setVerticalSpacing(6)
        
        # 创建一个全局控件
        wwg = QtWidgets.QWidget(self)
        wl = QtWidgets.QHBoxLayout(wwg)
        wl.addLayout(self.gridLayoutModuleSelect)
        wl.setContentsMargins(50, 200, 10, 10)

        self.gridLayout2 = QtWidgets.QGridLayout()
        
        self.button1 = QtWidgets.QPushButton(str(1), self)
        self.button2 = QtWidgets.QPushButton(str(2), self)
        self.button3 = QtWidgets.QPushButton(str(3), self)
        self.button4 = QtWidgets.QPushButton(str(4), self)

        self.gridLayout2.addWidget(self.button1, 0, 0)
        self.gridLayout2.addWidget(self.button2, 0, 1)
        self.gridLayout2.addWidget(self.button3, 1, 0)
        self.gridLayout2.addWidget(self.button4, 1, 1)

        wwg2 = QtWidgets.QWidget(self)
        wl2 = QtWidgets.QHBoxLayout(wwg2)
        wl2.addLayout(self.gridLayout2)
    
    def radioButtonFuc(self):
        print(self.radioGroup.checkedButton().text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = TestRadio()
    sys.exit(app.exec_())