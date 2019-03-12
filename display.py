#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtWidgets, QtCore
import json

ChipModelList = ["MH1901", "MH1902", "MH1903"]

class display(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ChipModuleList = ["ADC", "UART", "SPI", "KeyBoard", "LCD", "DCMI", "PWM", "MIPI", "SCI", "I2C",
                "SDRAM", "SDIO", "PSRAM"]
        self.initUI()

    def initUI(self):
        
        self.ModuleSelect()
        self.ChipModelSelect()
        self.resize(700, 500)
        self.move(20, 50)
        self.setWindowTitle("Param Display")
        self.show()

    def ChipModelSelect(self):
        self.ComboBoxChipModelSelect = QtWidgets.QComboBox(self)
        self.ComboBoxChipModelSelect.move(20, 50)
        self.ComboBoxChipModelSelect.addItems(ChipModelList)
        self.ComboBoxChipModelSelect.activated.connect(self.SetTableWidgetShow)

    def ModuleSelect(self):
        # self.ModuleParamShow({})
        self.ComboBoxModuleSelect = QtWidgets.QComboBox(self)
        self.ComboBoxModuleSelect.move(20, 90)
        # TODO: 
        self.ComboBoxModuleSelect.addItems(self.ChipModuleList)
        self.ComboBoxModuleSelect.activated.connect(self.SetTableWidgetShow)


    def ModuleParamShow(self, StructData):
        self.tempList = StructData.keys()
        print(self.tempList)
        
        self.tableWidgetShowIOStruct = QtWidgets.QTableWidget(self)
        self.VBoxLayout = QtWidgets.QGridLayout(self)
        
        self.ChipModuleSelectWidget = QtWidgets.QWidget(self)
        self.ChipModuleSelectLayout = QtWidgets.QHBoxLayout(self.ChipModuleSelectWidget)
        self.ChipModuleSelectLayout.addLayout(self.VBoxLayout)
        self.ChipModuleSelectLayout.setContentsMargins(50, 200, 10, 10)
        # self.ChipModuleSelectLayout.addWidget(self.tableWidgetShowIOStruct)
        self.VBoxLayout.addWidget(self.tableWidgetShowIOStruct)

        # 设置行数
        self.tableWidgetShowIOStruct.setRowCount(4)
        # 设置每一行的高度
        self.tableWidgetShowIOStruct.setRowHeight(0, 1)
        self.tableWidgetShowIOStruct.setRowHeight(1, 1)
        self.tableWidgetShowIOStruct.setRowHeight(2, 2)
        # 设置每一行的标签
        self.tableWidgetShowIOStruct.setVerticalHeaderLabels(["l1", "l2", "l3", "l4"])
        # 设置列数
        self.tableWidgetShowIOStruct.setColumnCount(3)
        # 设置每一列的宽度
        self.tableWidgetShowIOStruct.setColumnWidth(0, 70)
        self.tableWidgetShowIOStruct.setColumnWidth(1, 50)
        self.tableWidgetShowIOStruct.setColumnWidth(2, 70)
        self.newItem = QtWidgets.QTableWidgetItem("A")
        self.tableWidgetShowIOStruct.setItem(0, 0, self.newItem)
        # 设置每一列的标签
        self.tableWidgetShowIOStruct.setHorizontalHeaderLabels(["Group", "Pin", "Remap"])

    def GetStructFromFile(self):
        if os.path.exists(self.ComboBoxChipModelSelect.currentText() + "Data.json"):
            with open(self.ComboBoxChipModelSelect.currentText() + "Data.json", "r") as FileRead:
                return json.loads(FileRead.readline())
        else:
            return {}


    def SetTableWidgetShow(self):
        tmpModuleName = self.ComboBoxModuleSelect.currentText()
        tmpStruct = self.GetStructFromFile()
        if tmpModuleName not in tmpStruct:
            print("No Module Data")
        else:
            print(tmpStruct[tmpModuleName])
            self.ModuleParamShow(tmpStruct[tmpModuleName])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    displaytest = display()
    sys.exit(app.exec_())