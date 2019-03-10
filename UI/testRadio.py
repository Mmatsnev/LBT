#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore

class TestRadio(QtWidgets.QWidget):
    def __init__(self, ModuleList, IOGroupNumber):
        super().__init__()
        self.ChipModuleList = ModuleList
        self.ChipIOGroupList = [chr(index + 65) for index in range(IOGroupNumber)]
        self.textShowStruct = {"ChipModel": "-", "Module": "-", "IOGroup": "-", "IOPin": "-", "IORemap": "-", "管脚作用": "-"}

        self.initUI()
        

    def initUI(self):
        
        self.ChipIOParamInputUI()
        self.ShowParamUI()
        self.ChipModuleSelectUI()
        self.ChipModelSelectUI()
        self.pushButtonConfirmAdd = QtWidgets.QPushButton("确认添加", self)
        self.pushButtonConfirmAdd.resize(200, 200)
        self.pushButtonConfirmAdd.move(400, 100)

        self.resize(900, 600)
        self.move(50, 100)
        self.setWindowTitle("Test Radio")
        self.show()

    def ChipModuleSelectUI(self):
        # 创建一个grid 布局
        self.gridLayoutModuleSelect = QtWidgets.QGridLayout()
        self.gridLayoutModuleSelect.setObjectName("gridLayoutModuleSelect")

        # 创建一个radioGroup
        self.radioGroupModuleSelect = QtWidgets.QButtonGroup(self)

        # 把gridgroup 信号连接到槽
        self.radioGroupModuleSelect.buttonClicked.connect(self.SetTextEditText)
        # 设置grid 布局中相邻控件的间隔
        self.gridLayoutModuleSelect.setHorizontalSpacing(6)
        self.gridLayoutModuleSelect.setVerticalSpacing(6)
        
        # 创建一个全局控件
        self.ChipModuleSelectWidget = QtWidgets.QWidget(self)
        self.ChipModuleSelectLayout = QtWidgets.QHBoxLayout(self.ChipModuleSelectWidget)
        self.ChipModuleSelectLayout.addLayout(self.gridLayoutModuleSelect)
        self.ChipModuleSelectLayout.setContentsMargins(50, 100, 10, 10)

        gridLayoutRow = 0
        gridLayoutCol = 0
        # 把list 列表中的模块名称创建对应的Radio 按钮
        # 把创建的模块Radio 按钮添加到grid 布局中，同时添加到radio 组中。
        self.ChipModuleSelectRadioNames = self.__dict__
        for i in range(len(self.ChipModuleList)):
            self.ChipModuleSelectRadioNames['radioButton' + self.ChipModuleList[i]] = QtWidgets.QRadioButton(self.ChipModuleList[i], self)
            self.radioGroupModuleSelect.addButton(self.ChipModuleSelectRadioNames['radioButton' + self.ChipModuleList[i]])
            self.gridLayoutModuleSelect.addWidget(self.ChipModuleSelectRadioNames['radioButton' + self.ChipModuleList[i]], gridLayoutRow, gridLayoutCol)
            gridLayoutCol += 1
            if gridLayoutCol == 4:
                gridLayoutCol = 0
                gridLayoutRow += 1

    def ChipIOParamInputUI(self):
        self.labelIOParamModule = QtWidgets.QLabel("Module", self)
        self.labelIOParamGroup = QtWidgets.QLabel("Group", self)
        self.labelIOParamPin = QtWidgets.QLabel("Pin", self)
        self.labelIOParamRemap = QtWidgets.QLabel("Remap", self)

        self.lineEditIOParamModule = QtWidgets.QLineEdit(self)
        self.lineEditIOParamModule.setMaxLength(20)
        self.lineEditIOParamModule.textChanged.connect(self.SetTextEditText)

        self.gridLayoutIOParamInput = QtWidgets.QGridLayout()
        self.gridLayoutIOParamInput.setObjectName("gridLayoutIOParamInput")

        # 创建一个grid 布局
        self.gridLayoutIOGroupSelect = QtWidgets.QGridLayout()
        self.gridLayoutIOGroupSelect.setObjectName("gridLayoutIOGroupSelect")

        self.gridLayoutIOPinSelect = QtWidgets.QGridLayout()
        self.gridLayoutIOPinSelect.setObjectName("gridLayoutIOPinSelect")

        self.gridLayoutIORemapSelect = QtWidgets.QGridLayout()
        self.gridLayoutIORemapSelect.setObjectName("gridLayoutIORemapSelect")

        # 创建一个radioGroup
        self.radioGroupIOGroupSelect = QtWidgets.QButtonGroup(self)
        self.radioGroupIOPinSelect = QtWidgets.QButtonGroup(self)
        self.radioGroupIORemapSelect = QtWidgets.QButtonGroup(self)

        # 把gridgroup 信号连接到槽
        self.radioGroupIOGroupSelect.buttonClicked.connect(self.SetTextEditText)
        self.radioGroupIOPinSelect.buttonClicked.connect(self.SetTextEditText)
        self.radioGroupIORemapSelect.buttonClicked.connect(self.SetTextEditText)
        # 设置grid 布局中相邻控件的间隔
        self.gridLayoutIOParamInput.setHorizontalSpacing(10)
        self.gridLayoutIOParamInput.setVerticalSpacing(20)

        self.gridLayoutIOGroupSelect.setHorizontalSpacing(6)
        self.gridLayoutIOGroupSelect.setVerticalSpacing(6)

        self.gridLayoutIOPinSelect.setHorizontalSpacing(6)
        self.gridLayoutIOPinSelect.setVerticalSpacing(6)

        self.gridLayoutIORemapSelect.setHorizontalSpacing(6)
        self.gridLayoutIORemapSelect.setVerticalSpacing(6)
        
        # 创建一个全局控件
        self.IOGroupSelectWidget = QtWidgets.QWidget(self)
        self.IOGroupSelectLayout = QtWidgets.QHBoxLayout(self.IOGroupSelectWidget)
        self.IOGroupSelectLayout.addLayout(self.gridLayoutIOParamInput)
        self.IOGroupSelectLayout.setContentsMargins(50, 200, 10, 10)

        self.gridLayoutIOParamInput.addWidget(self.labelIOParamModule, 0, 0)
        self.gridLayoutIOParamInput.addWidget(self.lineEditIOParamModule, 0, 1)

        self.gridLayoutIOParamInput.addWidget(self.labelIOParamGroup, 1, 0)
        self.gridLayoutIOParamInput.addLayout(self.gridLayoutIOGroupSelect, 1, 1)

        self.gridLayoutIOParamInput.addWidget(self.labelIOParamPin, 2, 0)
        self.gridLayoutIOParamInput.addLayout(self.gridLayoutIOPinSelect, 2, 1)

        self.gridLayoutIOParamInput.addWidget(self.labelIOParamRemap, 3, 0)
        self.gridLayoutIOParamInput.addLayout(self.gridLayoutIORemapSelect, 3, 1)


        gridLayoutRow = 0
        gridLayoutCol = 0
        # 把list 列表中的模块名称创建对应的Radio 按钮
        # 把创建的模块Radio 按钮添加到grid 布局中，同时添加到radio 组中。
        self.IOGroupSelectRadioNames = self.__dict__
        for i in range(len(self.ChipIOGroupList)):
            self.IOGroupSelectRadioNames['radioButton' + self.ChipIOGroupList[i]] = QtWidgets.QRadioButton(self.ChipIOGroupList[i], self)
            self.radioGroupIOGroupSelect.addButton(self.IOGroupSelectRadioNames['radioButton' + self.ChipIOGroupList[i]])
            self.gridLayoutIOGroupSelect.addWidget(self.IOGroupSelectRadioNames['radioButton' + self.ChipIOGroupList[i]], gridLayoutRow, gridLayoutCol)
            gridLayoutCol += 1
            if gridLayoutCol == 4:
                gridLayoutCol = 0
                gridLayoutRow += 1

        gridLayoutRow = 0
        gridLayoutCol = 0
        # 把list 列表中的模块名称创建对应的Radio 按钮
        # 把创建的模块Radio 按钮添加到grid 布局中，同时添加到radio 组中。
        self.IOPinSelectRadioNames = self.__dict__
        for i in range(16):
            self.IOPinSelectRadioNames['radioButton' + str(i)] = QtWidgets.QRadioButton(str(i), self)
            self.radioGroupIOPinSelect.addButton(self.IOPinSelectRadioNames['radioButton' + str(i)])
            self.gridLayoutIOPinSelect.addWidget(self.IOPinSelectRadioNames['radioButton' + str(i)], gridLayoutRow, gridLayoutCol)
            gridLayoutCol += 1
            if gridLayoutCol == 4:
                gridLayoutCol = 0
                gridLayoutRow += 1

        gridLayoutRow = 0
        gridLayoutCol = 0
        # 把list 列表中的模块名称创建对应的Radio 按钮
        # 把创建的模块Radio 按钮添加到grid 布局中，同时添加到radio 组中。
        self.IORemapSelectRadioNames = self.__dict__
        for i in range(4):
            self.IORemapSelectRadioNames['radioButton' + str(i)] = QtWidgets.QRadioButton(str(i), self)
            self.radioGroupIORemapSelect.addButton(self.IORemapSelectRadioNames['radioButton' + str(i)])
            self.gridLayoutIORemapSelect.addWidget(self.IORemapSelectRadioNames['radioButton' + str(i)], gridLayoutRow, gridLayoutCol)
            gridLayoutCol += 1
            if gridLayoutCol == 4:
                gridLayoutCol = 0
                gridLayoutRow += 1

    def ChipModelSelectUI(self):
        self.comboBoxChipModelSelect = QtWidgets.QComboBox(self)
        self.comboBoxChipModelSelect.addItem("MH1901")
        self.comboBoxChipModelSelect.addItem("MH1902")
        self.comboBoxChipModelSelect.addItem("MH1903")
        self.comboBoxChipModelSelect.activated.connect(self.SetTextEditText)

        self.comboBoxChipModelSelect.move(50, 50)

    def ShowParamUI(self):
        self.textEditShowParam = QtWidgets.QTextEdit(self)
        self.textEditShowParam.setReadOnly(True)
        self.textEditShowParam.resize(300, 100)
        self.textEditShowParam.move(50, 450)

    def SetTextEditText(self):
        if self.radioGroupModuleSelect.checkedButton():
            self.textShowStruct["Module"] = self.radioGroupModuleSelect.checkedButton().text()
        if self.radioGroupIOGroupSelect.checkedButton():
            self.textShowStruct["IOGroup"] = self.radioGroupIOGroupSelect.checkedButton().text()
        if self.radioGroupIOPinSelect.checkedButton():            
            self.textShowStruct["IOPin"] = self.radioGroupIOPinSelect.checkedButton().text()
        if self.radioGroupIORemapSelect.checkedButton():
            self.textShowStruct["IORemap"] = self.radioGroupIORemapSelect.checkedButton().text()
        self.textShowStruct["ChipModel"] = self.comboBoxChipModelSelect.currentText()
        if not self.lineEditIOParamModule.text():
            self.textShowStruct["管脚作用"] = "-"
        else:
            self.textShowStruct["管脚作用"] = self.lineEditIOParamModule.text()
        
        self.textEditShowParam.setText("芯片型号：%s\n模块：%s\n管脚作用：%s\nIO：P%s%s,Remap_%s"%(
            self.textShowStruct["ChipModel"], self.textShowStruct["Module"], self.textShowStruct["管脚作用"], 
            self.textShowStruct["IOGroup"], self.textShowStruct["IOPin"], self.textShowStruct["IORemap"]))
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    modulelist = ["ADC", "UART", "SPI", "KeyBoard", "LCD", "DCMI", "PWM", "MIPI", "SCI", "I2C",
                "SDRAM", "SDIO", "PSRAM"]
    
    test = TestRadio(modulelist, 8)
    sys.exit(app.exec_())