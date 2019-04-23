#!usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class DeleteBlankLine(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.setWindowTitle("DeleteBlankLine")
        self.DeleteBlankLineUI()

    def DeleteBlankLineUI(self):
        self.PushButtonSelectFile = QtWidgets.QPushButton(self)
        self.PushButtonSelectFile.setText("选择文件")
        self.PushButtonSelectFile.clicked.connect(self.SlotBottonChooseFile)

    def SlotBottonChooseFile(self):
        self.FileNameSelected, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "Bin Files (*.bin);;All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

        if self.FileNameSelected == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(self.FileNameSelected)
        print("文件筛选器类型: ",filetype)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = DeleteBlankLine()
    test.initUI()
    test.show()
    sys.exit(app.exec_())
