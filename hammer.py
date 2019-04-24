#usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from GenerateRandomNumbers_UI import GenerateRandom
from BinToString_UI import BinToString
from DeleteBlankLine_UI import DeleteBlankLine

class Hammer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.setWindowTitle("Hammer")
        self.mainUI()
        
    
    def mainUI(self):
        # 创建左侧列表
        self.leftlist = QtWidgets.QListWidget()
        # 左侧列表被选后发送信号给 display 槽
        self.leftlist.currentRowChanged.connect(self.display)

        # 创建右侧 widget
        self.RightStack = QtWidgets.QStackedWidget(self)

        # 左侧列表中增加元素
        self.leftlist.insertItem(0, "获得随机数")
        self.leftlist.insertItem(1, "bin转换为str数据")
        self.leftlist.insertItem(2, "删除空白行")

        # 实例化随机数类
        self.GenerateRandom = GenerateRandom()
        # 创建 QWidget 添加随机数实例
        self.stackRandom = QtWidgets.QWidget()
        self.stackRandom.setLayout(self.GenerateRandom.StackGenerateRandomNumbersUI())

        # 实例化 BinToString 类
        self.BinToString = BinToString()
        # 创建 QWidget 添加 BinToString 实例
        self.StackBinToString = QtWidgets.QWidget()
        self.StackBinToString.setLayout(self.BinToString.BinToStringUI())

        # 实例化 DeleteBlankLine 类
        self.DeleteBlankLine = DeleteBlankLine()
        # 创建 QWidget 添加 DeleteBlankLine 实例
        self.StackDeleteBlankLine = QtWidgets.QWidget()
        self.StackDeleteBlankLine.setLayout(self.DeleteBlankLine.DeleteBlankLineUI())

        # 右侧列表中增加元素
        self.RightStack.addWidget(self.stackRandom)
        self.RightStack.addWidget(self.StackBinToString)
        self.RightStack.addWidget(self.StackDeleteBlankLine)
        

        # 把左侧和右侧列表添加到 HBoxLayout 
        self.HBox = QtWidgets.QHBoxLayout(self)
        self.HBox.addWidget(self.leftlist)
        self.HBox.addWidget(self.RightStack)
        self.setLayout(self.HBox)
        

    def display(self, i):
        print("当前索引：", i)
        self.RightStack.setCurrentIndex(i)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hammer = Hammer()
    hammer.initUI()
    hammer.show()
    sys.exit(app.exec_())
